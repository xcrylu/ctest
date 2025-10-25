import json
import os
import sys
import random
import test_exe as test
import zipfile
import hashlib
import tempfile

def generate_random_data(n, m, ranges):
    '''
    函数名： generate_random_data
    参数：
        n: 数据组数
        m: 每组数据个数
        ranges: 每个数据的取值范围列表，格式为[(min1, max1), (min2, max2), ..., (minm, maxm)]
    功能: 生成n组随机数据，每组包含m个随机整数，且每个整数在对应的范围内
    输出格式：
        第一行输出数据组数n
        接下来的n行，每行输出m个随机整数，整数之间用空格分隔  
    示例调用：
        generate_random_data(5, 3, [(1, 10), (20, 30), (100, 200)])
    返回：        
        [[3 25 150],
        [7 22 180],
        [1 30 120],
        [10 21 199],
        [5 28 130]]
    '''
    # 输出数据组数n
    if len(ranges) != m:
        raise ValueError(f"范围数量错误: 预期 {m} 个范围，但收到 {len(ranges)} 个范围")
    # print(n)
    results = []
    for _ in range(n):
        group = []
        for (min_val, max_val) in ranges:
            if(min_val > max_val):
                raise ValueError(f"范围错误: min({min_val}) 不能大于 max({max_val})")
            num = random.randint(min_val, max_val)
            group.append(str(num))
        # print(" ".join(group))
        results.append(group)

    return results



def set_testcase_input_data(jsonFilename,inputData=[]):
    '''
    更新测试用例文件中的输入数据
    参数：
        filename: 测试用例文件名（不含扩展名）
        data: 新的输入数据列表，每个元素为一组输入数据的字符串列表
    '''

    #  读取已有的测试用例文件
    with open(jsonFilename, "r", encoding="utf-8") as f:
        jsonData =json.load(f)

    count = jsonData['testCases']['count']

    # 更新测试用例输入数据
    for(i,datum) in enumerate(inputData):
        if i>=count:
            break
        # 更新测试用例输入数据
        jsonData['testCases']['data'][str(i+1)]['input'] = datum
    
    # 写回更新后的测试用例文件
    with open(jsonFilename, "w", encoding="utf-8") as f:
        json.dump(jsonData, f, ensure_ascii=False, indent=4)


def get_testcase_expected_result(prog,jsonfilename):
    test_data = test.read_testcases(jsonfilename)
    retdata = []
    for i in range(test_data["testCases"]["count"]):
        ret = test.run_exe(prog,input=test_data["testCases"][str(i+1)]["input"])
        retdata.append(ret.stdout)
    
    return retdata


def set_testcase_expected_reuslt(jsonFilename,expectedResult=[]):
    '''
    更新测试用例文件中的预期结果数据
    参数：
        filename: 测试用例文件名（不含扩展名）
        expectedData: 新的预期结果数据列表，每个元素为一组预期结果
    '''
    # 读取已有的要更新的测试用例文件
    with open(jsonFilename, "r", encoding="utf-8") as f:
        jsonData =json.load(f)   

    count = jsonData['testCases']['count']
    # print(expectedResult)

    # 更新测试用例期望输出数据
    for(i,datum) in enumerate(expectedResult):
        if i>=count:
            break
        # 更新测试用例输入数据
        jsonData['testCases']['data'][str(i+1)]['expectedResult'] = datum
    
    # 写回更新后的测试用例文件     
    with open(jsonFilename, "w", encoding="utf-8") as f:
        json.dump(jsonData, f, ensure_ascii=False, indent=4)


def create_json_test_case(filename,description="",count=0,inputdata=[],expectedResult=[]):
   
    # 模板文件
    JSONMODEFILE="/home/xcr/test/ctest/testcase/template.json"
    if len(inputdata) < count or len(expectedResult) < count:
        print("输入数据或期望结果数量量不足。")
        return False

    data={}
    try:
        with open(JSONMODEFILE,'r', encoding='utf-8') as f:
            data= json.load(f)
    except Exception as e:
            print(f"打开json模板文件发生错误：{str(e)}")
    
    data['testCases']['description']=description
    data['testCases']['count'] = count
   
    for i in range(count):
        tmp = {'input': inputdata[i],'expectedResult':expectedResult[i]}
        data['testCases']['data'][str(i+1)]=tmp
    
    try:
        with open(filename,'w', encoding='utf-8') as f:
            json.dump(data,f, ensure_ascii=False, indent=2)          
    except Exception as e:
            print(f"写json文件 '{filename}' 发生错误：{str(e)}")
    # print(data)
    return True


def zip_folder(source_folder, target_zip):
    """
    压缩源文件夹中的所有文件（包括子文件夹）到目标zip文件
    :param source_folder: 要压缩的源文件夹路径（绝对路径或相对路径）
    :param target_zip: 目标zip文件路径（如：./output.zip）

    示例用法:
      # 要压缩的源文件夹（可以是相对路径或绝对路径）
#     source = "./my_folder"  # 假设当前目录下有my_folder文件夹
#     # 目标zip文件路径
#     target = "./my_folder.zip"
#     # 调用函数压缩
#     zip_folder(source, target)
    """
    # 确保源文件夹存在
    if not os.path.isdir(source_folder):
        raise ValueError(f"源文件夹不存在：{source_folder}")
    
    # 创建并打开目标zip文件（模式'w'表示写入，ZIP_DEFLATED表示启用压缩）
    with zipfile.ZipFile(target_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # 递归遍历源文件夹
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                # 拼接文件的绝对路径（用于读取文件）
                file_path = os.path.join(root, file)
                # 计算文件在zip中的相对路径（保留目录结构）
                # 例如：源文件夹是'./data'，文件是'./data/sub/a.txt'，则相对路径为'sub/a.txt'            
                # arcname = os.path.relpath(file_path, os.path.dirname(source_folder))              
                arcname = os.path.relpath(file_path, source_folder)
                # 将文件添加到zip中（arcname指定在zip中的路径）
                zipf.write(file_path, arcname=arcname)
                # print(f"已添加到zip：{arcname}")
    
    print(f"压缩完成,目标文件：{target_zip}")


def create_qingline_testcase(testcasejsonfile,outputdir):
    '''
    根据json格式测试文件,
      对每个测试用例 ,
      生成：
        测试输入文件: x.in
        测试输出文件: x.out
     然后将所有测试用例输入输出文件打包压缩成zip格式的xx.zip文件
    '''
    # 检查目录是否存在
    if not os.path.isdir(outputdir):
       raise ValueError(f"源文件夹不存在：{outputdir}")
    
    # 读取测试用例json文件
    testcase = test.read_testcases(testcasejsonfile)   
    count = testcase["count"]

     # 创建测试文件，输入文件名：xx.in，输出文件名：xx.out
    with tempfile.TemporaryDirectory() as temp_dir:
        # 创建测试文件，输入文件名：xx.in，输出文件名：xx.out
        for i in range(count):
            # 创建.in文件
            # infile= "/home/xcr/test/ctest/tmp/"+str(i+1)+".in"    
            infile = os.path.join(temp_dir,str(i+1)+".in")
            try:
                with open(infile,'w',encoding='utf-8')  as f:
                    data =  testcase["input"][i]
                    f.write(data)
            except Exception as e:
                print(f"写in文件时发生错误：{str(e)}")
            
            # 创建.out文件
            # infile= "/home/xcr/test/ctest/tmp/"+str(i+1)+".out"
            infile = os.path.join(temp_dir,str(i+1)+".out")
            try:
                with open(infile,'w',encoding='utf-8')  as f:
                    data =  testcase["expectedResult"][i]
                    f.write(data)
            except Exception as e:
                print(f"写out文件时发生错误：{str(e)}")
        
        # 压缩所有输入(.in)输出(.out)文件
        filename_with_ext = os.path.basename(testcasejsonfile)    
        filename_without_ext = os.path.splitext(filename_with_ext)[0]
        zipfilename=os.path.join(outputdir,filename_without_ext+".zip")
        zip_folder(temp_dir,zipfilename)

    return True



def get_file_md5(file_path, chunk_size=4096):
    """计算文件的MD5值，chunk_size为分块大小（默认4KB）"""
    try:
        md5 = hashlib.md5()  # 创建MD5对象
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)  # 分块读取
                if not chunk:  # 读取完毕
                    break
                md5.update(chunk)  # 更新MD5
        return md5.hexdigest()  # 返回16进制结果
    except FileNotFoundError:
        return f"错误：文件 '{file_path}' 不存在"
    except PermissionError:
        return f"错误：没有权限访问文件 '{file_path}'"

# 测试
# file_path = "test.txt"  # 替换为你的文件路径
# print(f"文件MD5值：{get_file_md5(file_path)}")


def create_oj_testcase(testcasejsonfile,outputdir):
    '''
    根据json格式测试文件,
      对每个测试用例 ,
      生成：
        测试输入文件: x.in
        测试输出文件: x.out
     然后将所有测试用例输入输出文件打包压缩成zip格式的xx.zip文件
    '''
    # 检查目录是否存在
   
    if not os.path.isdir(outputdir):
       raise ValueError(f"源文件夹不存在：{outputdir}")
    
    # 读取测试用例json文件
    testcase = test.read_testcases(testcasejsonfile)   
    count = testcase["count"]
    
    # 打开oj json文件，
    ojdata=[]
    ojfilepath = '/home/xcr/test/ctest/testcase/oj-template.json'
    try:
        with open(ojfilepath,'r',encoding='utf-8') as f:
            ojdata= json.load(f)
    except  Exception as e:
        print(f"读 oj-template.json文件时发生错误：{str(e)}")
    
   
    # 创建测试文件，输入文件名：xx.in，输出文件名：xx.out
    with tempfile.TemporaryDirectory() as temp_dir:

        for i in range(count):
            
            # 创建.in文件
            # infile = "/home/xcr/test/ctest/oj/"+str(i+1)+".in"     
            infile= os.path.join(temp_dir, str(i+1)+".in") #"/home/xcr/test/ctest/oj/"+str(i+1)+".in"         
            try:
                with open(infile,'w',encoding='utf-8')  as f:
                    data =  testcase["input"][i]
                    f.write(data)              
            except Exception as e:
                print(f"写in文件时发生错误：{str(e)}")    
    
            
            # 创建.out文件
            # outfile= "/home/xcr/test/ctest/oj/"+str(i+1)+".out"
            outfile = os.path.join(temp_dir,str(i+1)+'.out')
        
            try:
                with open(outfile,'w',encoding='utf-8')  as f:
                    data =  testcase["expectedResult"][i]
                    f.write(data)
            except Exception as e:
                print(f"写out文件时发生错误：{str(e)}")
        
            outfilemd5  = get_file_md5(outfile)
            # print(outfilemd5)
            outfilesize = os.path.getsize(outfile)
            infilesize = os.path.getsize(infile)

            jsonNode = {
                            "stripped_output_md5": outfilemd5,                   
                            "input_name": f"{i+1}.in",
                            "input_size": infilesize,
                            "output_name": f"{i+1}.out",
                            "output_size": outfilesize,
                        }
            ojdata['test_cases'][f'{i+1}'] = jsonNode

        with open(os.path.join(temp_dir,"info"),'w',encoding='utf-8') as f:
            json.dump(ojdata,f, ensure_ascii=False, indent=2)

        # 將測試文件和info壓成zip文件
        filename_with_ext = os.path.basename(testcasejsonfile)    
        filename_without_ext = os.path.splitext(filename_with_ext)[0]
        # zipfilename='/home/xcr/test/ctest/oj_testcase/'+filename_without_ext+".zip"
        zipfilename=os.path.join(outputdir,filename_without_ext+".zip")
        zip_folder(temp_dir,zipfilename)

    return True


def create_all_zip_testcase():
    all_entries = os.listdir("/home/xcr/test/ctest/testcase/")
    all_entries.remove('oj-template.json')
    all_entries.remove('template.json')
    all_entries.remove('test.json')
    # print(all_entries)
    for file in all_entries:
        file = '/home/xcr/test/ctest/testcase/'+ str(file)
        # qingline格式测试用例
        create_qingline_testcase(file,'/home/xcr/test/ctest/qingline_testcase')
        # oj格式测试用例
        create_oj_testcase(file,'/home/xcr/test/ctest/oj_testcase')
        
    print("成功创建测试用例")

def generate_testcase_5():
    # 生成题 5 测试用例
    jsonfile = "./testcase/5.json"   
    prog_path = "./bin/5"

    # 产生测试输入
    data = []
    for i in range(10):
        num = random.randint(3, 60)
        data.append(str(num))
    set_testcase_input_data(jsonfile,data)
    print(f"输入数据：{data}")
    # 设置测试期望输出
    res = test.test(prog_path,jsonfile)   
    print(f"期望输出{res['output']}")
    set_testcase_expected_reuslt(jsonfile,res['output'])

def generate_testcase_8():
    # 生成题 5 测试用例
    jsonfile = "./testcase/8.json"   
    prog_path = "./bin/8"

    # 产生测试输入
    data = []
    for i in range(10):
        num =random.randint(100,200)
        data.append(str(num))

    random.shuffle(data)
    print(f"输入数据：{data}")
    set_testcase_input_data(jsonfile,data)   
   
    # 设置测试期望输出
    res = test.test(prog_path,jsonfile)   
    print(f"期望输出{res['output']}")
    set_testcase_expected_reuslt(jsonfile,res['output'])

def generate_testcase_9():
    # 生成题 5 测试用例
    jsonfile = "./testcase/9.json"   
    prog_path = "./bin/9"

    # 产生测试输入
    data = []
    for count in range(10):
        # 每一组数据
        num =random.randint(1,5)        
        datagroup = [str(num)+'\n']     
        for line in range(num):
            # 每一行数据
            dataline= []
            for col in range(num):
                # 每一列数据
                d = random.randint(-100,100)
                dataline.append(str(d))
            datalinestr = " ".join(dataline)+"\n"
            datagroup.append(datalinestr)        
        datagroupstr = ''.join(datagroup)# print(datagroup)     
        data.append(datagroupstr)
    
    print(data)

    # random.shuffle(data)
    # print(f"输入数据：{data}")
    set_testcase_input_data(jsonfile,data)   
   
    # 设置测试期望输出
    res = test.test(prog_path,jsonfile)   
    print(f"期望输出{res['output']}")
    set_testcase_expected_reuslt(jsonfile,res['output'])

def set_testcase_expectedResult():

    jsonfile = "./testcase/4.json"   
    prog_path = "./bin/4"  
    res = test.test(prog_path,jsonfile)   
    set_testcase_expected_reuslt(jsonfile,res['output'])

def main():
    # generate_testcase_9()
    # jsonfile  = './testcase/9.json'
    # create_zipfile_type_testcase(jsonfile)
    create_all_zip_testcase()
    # indata = ['1','2','3','4']
    # expdata= ['11','12','13','14']
    # create_json_test_case("/home/xcr/test/ctest/testcase/test.json","test description",4,indata,expdata)
    # create_oj_zipfile_type_testcase("/home/xcr/test/ctest/testcase/1.json")
    # print(get_file_md5('/home/xcr/test/ctest/oj/1.out'))


if __name__ == "__main__":   
    main()
