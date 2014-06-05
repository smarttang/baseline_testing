#coding:utf-8
import os,sys,getopt,ftplib,tarfile,ConfigParser,re
from xml.dom import minidom,Node
from lib.ReportAnaly import ReportAnaly
reload(sys)
sys.setdefaultencoding('utf8')

def print_read():
    print '''
=================================================================================
                       ::
                      :;J7, :,                        ::;7:
                      ,ivYi, ,                       ;LLLFS:
                      :iv7Yi                       :7ri;j5PL
                     ,:ivYLvr                    ,ivrrirrY2X,
                     :;r@Wwz.7r:                :ivu@kexianli.
                    :iL7::,:::iiirii:ii;::::,,irvF7rvvLujL7ur
                   ri::,:,::i:iiiiiii:i:irrv177JX7rYXqZEkvv17
                ;i:, , ::::iirrririi:i:::iiir2XXvii;L8OGJr71i
              :,, ,,:   ,::ir@mingyi.irii:i:::j1jri7ZBOS7ivv,
                 ,::,    ::rv77iiiriii:iii:i::,rvLq@huhao.Li
             ,,      ,, ,:ir7ir::,:::i;ir:::i:i::rSGGYri712:
           :::  ,v7r:: ::rrv77:, ,, ,:i7rrii:::::, ir7ri7Lri
          ,     2OBBOi,iiir;r::        ,irriiii::,, ,iv7Luur:
        ,,     i78MBBi,:,:::,:,  :7FSL: ,iriii:::i::,,:rLqXv::
        :      iuMMP: :,:::,:ii;2GY7OBB0viiii:i:iii:i:::iJqL;::
       ,     ::::i   ,,,,, ::LuBBu BBBBBErii:i:i:i:i:i:i:r77ii
      ,       :       , ,,:::rruBZ1MBBqi, :,,,:::,::::::iiriri:
     ,               ,,,,::::i:  @arqiao.       ,:,, ,:::ii;i7:
    :,       rjujLYLi   ,,:::::,:::::::::,,   ,:i,:,,,,,::i:iii
    ::      BBBBBBBBB0,    ,,::: , ,:::::: ,      ,,,, ,,:::::::
    i,  ,  ,8BMMBBBBBBi     ,,:,,     ,,, , ,   , , , :,::ii::i::
    :      iZMOMOMBBM2::::::::::,,,,     ,,,,,,:,,,::::i:irr:i:::,
    i   ,,:;u0MBMOG1L:::i::::::  ,,,::,   ,,, ::::::i:i:iirii:i:i:
    :    ,iuUuuXUkFu7i:iii:i:::, :,:,: ::::::::i:i:::::iirr7iiri::
    :     :rk@Yizero.i:::::, ,:ii:::::::i:::::i::,::::iirrriiiri::,
     :      5BMBBBBBBSr:,::rv2kuii:::iii::,:i:,, , ,,:,:i@petermu.,
          , :r50EZ8MBBBBGOBBBZP7::::i::,:::::,: :,:,::i;rrririiii::
              :jujYY7LS0ujJL7r::,::i::,::::::::::::::iirirrrrrrr:ii:
           ,:  :@kevensun.:,:,,,::::i:i:::::,,::::::iir;ii;7v77;ii;i,
           ,,,     ,,:,::::::i:iiiii:i::::,, ::::iiiir@xingjief.r;7:i,
        , , ,,,:,,::::::::iiiiiiiiii:,:,:::::::::iiir;ri7vL77rrirri::
         :,, , ::::::::i:::i:::i:i::,,,,,:,::i:i:::iir;@Secbone.ii:::

    [About me]
    =============
    Software: Baseline_testing
    Version:  V1.0
    Author: smarttang
    Github: Https://github.com/smarttang/

    [Usage]
    =============
        python Baseline_testing.py [option] [value]

    [Option]
    =============
        -h help How to check config?
        -n name (your name)
        -m mode (ftp) if you want to upload report,
                    input ftp_username,ftp_password,ftp_port,ftp_address 
                    in ini/ftp.ini,and -m ftp. if you don't want upload
                    Don't set -m option.
    [Demo]
    =============
        1) I want to check and output the html report.
            python Baseline_testing.py -n smart
        2) I want to check and output the html report,because I want upload ftp.
            python Baseline_testing.py -n smart -m ftp

==================================================================================
            '''

class Baseline_main:
    global doc,results_list,local_ip
    # xml 生成
    doc=minidom.Document()
    # 生成xml大名
    results_list=doc.createElement("baseline")
    doc.appendChild(results_list)
    local_ip=os.popen("ifconfig | grep inet | head -n1|awk -F \":\" '{print $2}'| awk '{print $1}'").readline().strip("\n")
    if len(local_ip)==0:
        local_ip="localhost"

    def __init__(self,output_name,mod=None):
        self.mod=mod
        self.plugins=[]
        self.output_name=output_name
        self.__loadPlugins()

    def __loadPlugins(self):
        checkPath=os.path.split(os.path.realpath(__file__))[0]
        if os.path.exists(checkPath+"/plugins"):
            for filename in os.listdir(checkPath+'/plugins'):
                if not filename.endswith('.py') or filename.startswith('_'):
                    continue
                self.__runPlugins(filename)
        else:
            print "[*] Plugins directory not in here!"
            print "[*] Done."

    def __runPlugins(self,filename):
        plugins_name=os.path.splitext(filename)[0]
        plugin=__import__("plugins."+plugins_name,fromlist=[plugins_name])
        clazz=plugin.getPluginClass()
        o=clazz()
        o.setBaseline_main(self)
        o.start()
        o.save()
        self.plugins.append(o)

    def xml_result(self,check_item):
        base_line = doc.createElement("module")
        base_line.setAttribute("mod_id",check_item['mod_id'])

        mod_name = doc.createElement("mod_name")
        mod_name.appendChild(doc.createTextNode(check_item['mod_name']))
        base_line.appendChild(mod_name)

        status_code = doc.createElement("status_code")
        status_code.appendChild(doc.createTextNode(check_item['status']))
        base_line.appendChild(status_code)

        mod_results = doc.createElement("mod_results")
        mod_results.appendChild(doc.createTextNode(check_item['results']))
        base_line.appendChild(mod_results)

        results_list.appendChild(base_line)

    def save_xml_html(self):
        for o in self.plugins:
            o.setBaseline_main(None)
        self.plugins=[]
        xml_path=os.path.split(os.path.realpath('__file__'))[0]+"/report/xml/"+local_ip+"_"+self.output_name+".xml"
        f=file(xml_path,"w")
        doc.writexml(f,"\t","\t","\n","utf-8")
        f.close()
        self.save_report(xml_path)

    def save_report(self,xml_path):
        doc=minidom.parse(xml_path)
        for child in doc.childNodes:
            html_path=os.path.split(os.path.realpath('__file__'))[0]+"/report/html/"+local_ip+"_"+self.output_name+".html"
            if child.nodeType == Node.ELEMENT_NODE:
                ReportAnaly(child,html_path)

        try:
            tar=tarfile.open(os.path.split(os.path.realpath('__file__'))[0]+"/report/tar/"+local_ip+"_"+self.output_name+".tar.gz","w|gz")
            tar.add(os.path.split(os.path.realpath('__file__'))[0]+"/report/html/"+local_ip+"_"+self.output_name+".html")
            tar.add(os.path.split(os.path.realpath('__file__'))[0]+"/report/xml/"+local_ip+"_"+self.output_name+".xml")
            tar.close()
        except:
            print "[*] Tar Error!! Chmod file or Make sure report is Here!!"
        
        if not self.mod==None:
            try:
                output_path=os.path.split(os.path.realpath('__file__'))[0]+"/report/html/"+local_ip+"_"+self.output_name+".html"
                cf=ConfigParser.ConfigParser()
                cf.read("ini/ftp.ini")
                ftp_ip=cf.get("ftp","ftp_ip")
                ftp_username=cf.get("ftp","ftp_username")
                ftp_password=cf.get("ftp","ftp_password")
                ftp_port=cf.get("ftp","ftp_port")
                ftp=ftplib.FTP()
                ftp.connect(ftp_ip,ftp_port)
                ftp.login(ftp_username,ftp_password)
                bufsize=2048
                file_handler=open(output_path,"rb")
                ftp.storbinary('STOR %s' % local_ip+"_"+self.output_name+".html",file_handler,bufsize)
                file_handler.close()
                ftp.quit()
                print "[*] Finish Baseline Testing!!"
            except:
                print "[*] FTP SAVE PUT ERROR!Please check your config: ini/ftp.ini !!"
        else:
            print "[*] Finish Baseline Testing!!"

if __name__=="__main__":
    global username,mode
    username=""
    mode=""
    try:
        options,args=getopt.getopt(sys.argv[1:],"hn:m:",["help","name=","mod="])
    except getopt.GetoptError:
        print_read()
        sys.exit()
    for name,value in options:
        if name in ("-h","--help"):
            print_read()
            sys.exit(1)
        if name in ("-n","--name"):
            username=value
        if name in ("-m","--mod"):
            mode=value
    if username:
        if mode=="ftp":
            obj=Baseline_main(username,mode)
            obj.save_xml_html()
        else:
            obj=Baseline_main(username)
            obj.save_xml_html()
    else:
        print_read()
