# python-leofile  make files to objects


leo do not like to use "os.path.join" <br/> 
so this tiny class borned<br/>

在遍历文件的时候被path.join绕晕了<br /> 
所以写了这个小工具<br /> 


    usage:
        path = '/etc'
        etcObj = Leofile(path)
        nginxConfObj = etcObj.nginx['nginx.conf'].open('r')
        nginxConfObj.read()
