import json
import os
import sys
import random
import zipfile
import hashlib
import subprocess
import json

class Test:
    # 类的属性（数据）和方法（函数）
    def __init__(self, prog, testcase):  # 初始化方法（构造函数）
        self.prog = prog  # 绑定实例属性
        self.input = []
        self.expectOutput=[]
        self.output=[]

        with open(testcase,'r',encoding='utf-8') as f:
            _testcase = json.load(f)

        self.testcase = _testcase    
        

        for key,value in self.testcase['testCases'] ['data'].items():
            # print(key)
            # print(value)
            self.input.append(value['input'])
            self.expectOutput.append(value['expectedResult'])

        self.result={"progameName": os.path.basename(prog),
                     "description":_testcase['testCases']['description'],
                     "successed": False,
                     "count":_testcase['testCases']['count'],
                     "input":self.input,
                     "expectOutput":self.expectOutput                    
                     }

    def test(self):  # 类的方法（第一个参数必须是self）
        # 方法体（可访问self.属性）
        for ipt,opt in zip(self.input,self.expectOutput):
            # print(ipt+'-->'+opt,end='')
            res = subprocess.run(
                [self.prog] ,
                input=ipt,
                capture_output=True,
                text=True
            )
            self.output.append(res.stdout.strip())
            # print('==>'+ res.stdout )
        
        self.result['output'] = self.output
        if self.output==self.expectOutput:
            self.result['successed'] = True
        
        self.printResult()
        return self.result
        # print(self.output)  


    def printResult(self):
        print(f"被测程序：{self.result['progameName']}\n")
        print(f"程序说明：{self.result['description']} \n")

        print( "      测试结果：✅ 通过\n" if self.result['successed']  else "测试结果：  ❌ 失败\n") 

        print("测试用例              输入数据   预期输出   实际输出    结果")
        print("---------------------------------------------------------------")
    
        total = len(self.result['expectOutput'])
        passed = 0
        for i in range(total):
            print(f" {i+1:>6}: {self.input[i].strip() if self.input[i].strip()=='' else '无输入':>20}  {self.expectOutput[i].strip():>10}  {self.output[i].strip().strip():>10} ", end='')
            if self.output[i].strip() == self.expectOutput[i].strip():
                print(" ✅ 通过")
                passed += 1
            else:
                print(" ❌ 失败")
        print("---------------------------------------------------------------")
        print(f"统计: {passed}/{total} 个测试用例通过。")
    

def main():
    for i in range(10):
        testprog = f'/home/xcr/test/ctest/bin/{i+1}'
        testcase = f'/home/xcr/test/ctest/testcase/{i+1}.json'
        test = Test(testprog,testcase)
        test.test()
 

if __name__ == "__main__":   
    main()