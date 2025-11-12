import os
import subprocess
import json

def run_exe(prog, params=None,input=None):
    '''
    封装一个函数来运行可执行文件并捕获输出
    prog: 可执行文件路径
    params: 传递给可执行文件的参数列表
    input: 传递给可执行文件的标准输入内容
    返回值: 包含stdout和stderr的CompletedProcess对象
    示例用法:
    result = run_exe("./my_program", ["arg1", "arg2"], input="some input\n")
    '''
    # print(input)
    result = subprocess.run(
        [prog] + (params if params else []),
        input=input,
        capture_output=True,
        text=True
    )
    return result



def read_testcases(json_file):
    '''
    读取指定JSON文件中的测试用例数据
    参数：
        json_file: JSON文件路径
    返回：
        包含所有测试用例输入和输出的数据列表
    示例用法：
        inputs = read_testcases("./testcase/1.json")
    备注：
        假设JSON文件结构如下：  
        {
        "testcases": {
            "counts": 3,
            "description: "two intergel add"
            "test_data": {  
                "1": {                  
                    "input": "5 10",
                    "expectedResult": "15"
                },
                "2": {                  
                    "input": "20 30",
                    "expectedResult": "50"
                },
                "3": {                   
                    "input": "100 200",
                    "expectedResult": "300"
                }
            }
        }
        返回结果：
        {
            "count": count,
            "description": "two intergel add",       
            "input": [
                "5 10",
                "20 30",
                "100 200"
            ],
            "expectedResult": [
                "15",
                "50",
                "300"
            ]    
        }

    '''
    # 获取文件名（不含路径）
    file_name = os.path.basename(json_file)
    # print(f"文件名：{file_name}\n")
    try:
        # 打开并加载JSON文件
        with open(json_file, 'r', encoding='utf-8') as f:
            jsonData = json.load(f)
        
        # 提取testcases字段（确保存在该字段）
        if 'testCases' not in jsonData:
            print(f"错误：{file_name}中未找到'testCases'字段")
            return

        testCases = jsonData['testCases']

        count = testCases.get('count', 0)        
        description = testCases.get('description', '')   

        data = testCases.get('data', {})
        # print(data)
        keys = data.keys()
        
        input = []       
        expectedResult = [] 

        for key in keys:       
            # 获取测试数据的输入值
            input.append(data.get(key, {}).get('input', ''))
            expectedResult.append(data.get(key, {}).get('expectedResult', ''))
               
        return {"description": description,"count": count,"input": input,"expectedResult": expectedResult}

    except FileNotFoundError:
        print(f"错误：文件'{json_file}'不存在")
    except json.JSONDecodeError:
        print(f"错误：{json_file}不是有效的JSON文件")
    except Exception as e:
        print(f"处理文件时发生错误：{str(e)}")


def test(test_prog,testcase_file):
    '''
    测试指定可执行文件与测试用例文件
    参数：
        test_prog: 可执行文件路径
        testcase_file: 测试用例JSON文件路径
    功能：
        读取测试用例文件中的输入和预期输出
        依次将输入传递给可执行文件运行
        比较可执行文件的输出与预期输出，返回测试结果
    示例用法：  
    '''  
    # 读取测试用例数据
    test_data = read_testcases(testcase_file)
    # print(test_data)
    test_input = test_data['input']
    test_expectedOutput = test_data['expectedResult']
    description = test_data['description']
   
    # 测试输出结果
    testOutput = []
    testres = []
    ok = False
    suc = 0
    failure = 0
    for input,expectedOutput in zip(test_input,test_expectedOutput):      
        # 运行可执行文件并捕获输出
        result = run_exe(test_prog, input=input)
        out = result.stdout.strip()
        testOutput.append(out)  
        if out.strip() == expectedOutput.strip():
            suc = suc+1
            testres.append(True)
        else:
            failure = failure + 1
            testres.append(False)
    ok = True if( failure == 0 ) else False        
    

    # 设置测试结果
    result = {"test_prog":test_prog,
              "description":description,
              "success": ok,
              "input": test_input, 
              "output": testOutput, 
              "expectedOutput": testOutput           
            }
    
    # 输出测试结果
    printTestResult(result)

    return result

def printTestResult(test_result):
    '''
    测试指定可执行文件与测试用例文件
    参数：
        test_prog: 可执行程序名称
        output: 可执行程序输出结果
        expectedOutput: 预期输出结果        
    '''
    inputdata = test_result['input']
    outputdata = test_result['output']  
    expectedOutput = test_result['expectedOutput']

    print(f"被测程序：{test_result['test_prog']}\n")
    print(f"程序说明：{test_result['description']} \n")

    print( "      测试结果：✅ 通过\n" if test_result['success']  else "测试结果：  ❌ 失败\n") 

    print("测试用例              输入数据   预期输出   实际输出    结果")
    print("---------------------------------------------------------------")
   
    total = len(test_result['expectedOutput'])
    passed = 0
    for i in range(total):
        print(f" {i+1:>6}: {inputdata[i].strip():>20}  {expectedOutput[i].strip():>10}  {outputdata[i].strip().strip():>10} ", end='')
        if outputdata[i].strip() == expectedOutput[i].strip():
            print(" ✅ 通过")
            passed += 1
        else:
            print(" ❌ 失败")
    print("---------------------------------------------------------------")
    print(f"统计: {passed}/{total} 个测试用例通过。")
    # print('测试结果：',end='')
    # if passed == total :
    #    print("全部通过 ✅" )
    # else:
    #     if passed == 0 :
    #         print(" 全部失败 ❌" )
    #     else:  
    #         print("部分通过 🟨")



def main():
    for i in range(10):
        test_prog = f"/home/xcr/test/ctest/bin/{i+1}"
        testcase_file = f"/home/xcr/test/ctest/testcase/{i+1}.json"
        res = test(test_prog,testcase_file)
    # test_run_exe()
    # test_generate_random_data()
    # test_zip_folder()
    # test_read_testcases()
    # printTestResult(res)
    # pass 
    # print(res['output'])  
    # print(res['expectedResult'])

if __name__ == "__main__":
    main()
    # test_read_testcases()