# encoding: utf-8
__license__ = 'MIT'
__all__=['FileUtils']

class FileUtils:
    @staticmethod
    def get_content(path,encoding = 'gbk'):
        """
        从指定路径的多个文件加载内容
        :param path: 文件路径
        :param encoding: 编码
        :return: 
        """
        
        with open(path, 'r', encoding= encoding,errors='ignore') as f:
            content = ''
            for l in f:
                l = l.strip()
                content += l
            return content

