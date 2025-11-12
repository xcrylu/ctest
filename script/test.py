from genericpath import isfile
import json
import os
import sys
import random
import zipfile
import hashlib
import subprocess
import json

class Test:
  
    def __init__(self, prog:str, testcase:str): 
        self.prog = prog  
        self.input = []
        self.expectOutput=[]
        self.output=[]
        # 获取测试数据
        with open(testcase,'r',encoding='utf-8') as f:
            _testcase = json.load(f)

        self.testcase = _testcase            
        #整理json数据改成列表
        for key,value in self.testcase['testCases'] ['data'].items():
            self.input.append(value['input'])
            self.expectOutput.append(value['expectedResult'])
        # 准备测试结果
        self.result={"progameName": os.path.basename(prog),
                     "description":_testcase['testCases']['description'],
                     "successed": False,
                     "count":_testcase['testCases']['count'],
                     "input":self.input,
                     "expectOutput":self.expectOutput                    
                     }

    def test(self):  
        # 测试每个测试用例       
        for ipt,opt in zip(self.input,self.expectOutput):         
            res = subprocess.run(
                [self.prog] ,
                input=ipt,
                capture_output=True,
                text=True
            )
            self.output.append(res.stdout.strip())
       
        # 保存测试结果
        self.result['output'] = self.output
        suc = True
        for opt,exp in zip( self.output,self.expectOutput):
            if opt.strip() != exp.strip():
                suc = False
                break       
        self.result['successed'] = suc
      
        return self.result
       

    def reportTestResult(self,filename):
        # 生成测试报告文件
        with open(filename,"a",encoding='utf-8') as f:

            f.write(f"\n被测程序 ：{os.path.basename(self.prog)} \n程序功能：{self.result['description']}\n")
            f.writelines('\n')

            f.write( "\t最终测试结果： " + '通过 ✅ \n'  if self.result['successed'] else ' 失败❌\n')           
            f.write('\n')

            f.write("测试详情：\n===============================================\n")
            i = 1
            for ipt ,opt ,should in zip(self.input,self.output,self.expectOutput):                
                f.write(f'第{i}组数据：')                
               
                f.write( '通过 ✅\n' if opt.strip() == should.strip() else '\t失败❌\n')
                f.write("---------------------------\n")   
                f.write(f"输入:{ipt}\n")
                f.write(f"输出:\n{opt}\n")
                f.write(f"正确输出:\n{should}\n\n")                           
                
                i = i+1   

    def printResult(self):
        # 打印测试结果
        print(f"\n被测程序：{self.result['progameName']}")
        print(f"程序说明：{self.result['description']}")

        print( "      测试结果：✅ 通过\n" if self.result['successed']  else "测试结果：  ❌ 失败") 

        print("测试用例              输入数据   预期输出   实际输出    结果")
        print("---------------------------------------------------------------")
    
        total = len(self.result['expectOutput'])
        passed = 0
        for i in range(total):
            print(f" {i+1:>6}: {self.input[i].strip() if self.input[i].strip()=='' else '无':>20}  {self.expectOutput[i].strip():>10}  {self.output[i].strip().strip():>10} ", end='')
            if self.output[i].strip() == self.expectOutput[i].strip():
                print(" ✅ 通过")
                passed += 1
            else:
                print(" ❌ 失败")
        print("---------------------------------------------------------------")
        print(f"统计: {passed}/{total} 个测试用例通过。")
    

def main():
    reportfile = "report.txt"
    if os.path.isfile(reportfile):
        os.remove(reportfile)

    for i in range(10):
        testprog = f'/home/xcr/test/ctest/bin/{i+1}'
        testcase = f'/home/xcr/test/ctest/testcase/{i+1}.json'
        test = Test(testprog,testcase)
        test.test()
        test.reportTestResult(reportfile)
        
 

if __name__ == "__main__":   
    main()