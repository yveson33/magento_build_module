#!/usr/bin/python

import subprocess
import optparse
import os

PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))
LOCAL_DIR = os.path.join(PROJECT_PATH, "app/code/local")
ETC_MODULES_PATH = os.path.join(PROJECT_PATH, "app/etc/modules")

parser = optparse.OptionParser()
parser.add_option('-n', '--namespace',
    help="namespace")
parser.add_option('-m', '--module',
    help="module")

options, args = parser.parse_args()

namespace = options.namespace.title()
module = options.module.title()

NAMESPACE_DIR = os.path.join(LOCAL_DIR, namespace)
MODULE_DIR = os.path.join(LOCAL_DIR, NAMESPACE_DIR, module)

configxml = ""
configxml += "<config>\n\t"
configxml += "<modules>\n\t\t"
configxml += "<{0}_{1}>\n\t\t\t".format(namespace, module)
configxml += "<version>0.1.0</version>\n\t\t"
configxml += "</{0}_{1}>\n\t".format(namespace, module)
configxml += "</modules>\n"
configxml += "</config>\n"

namespace_module_xml = ""
namespace_module_xml += "<config>\n\t"
namespace_module_xml += "<modules>\n\t\t"
namespace_module_xml += "<{0}_{1}>\n\t\t\t".format(namespace, module)
namespace_module_xml += "<active>true</active>\n\t\t\t"
namespace_module_xml += "<codePool>local</codePool>\n\t\t"
namespace_module_xml += "</{0}_{1}>\n\t".format(namespace, module)
namespace_module_xml += "</modules>\n"
namespace_module_xml += "</config>\n"

def buildModule(path_to_local_dir, namespace_dir, module_dir):
	if os.path.exists(os.path.join(path_to_local_dir, namespace_dir, module_dir)):
		print ("module dir always exists") 
	else: 
		try:
			os.mkdir(namespace_dir)
			os.mkdir(module_dir)
			# created module sub dirs
			os.mkdir(os.path.join(module_dir, 'Controller'))
			os.mkdir(os.path.join(module_dir, 'controllers'))
			os.mkdir(os.path.join(module_dir, 'etc'))
			os.mkdir(os.path.join(module_dir, 'Helper'))
			os.mkdir(os.path.join(module_dir, 'Model'))
			os.mkdir(os.path.join(module_dir, 'sql'))
			#created module config.xml file
			config_filename = os.path.join(os.path.join(module_dir, 'etc'), "config.xml")
			config_file = open(config_filename, 'w+')
			config_file.write(configxml)
			config_file.close()
		except Exception, e:
			raise

if __name__ == '__main__':
	if os.path.exists(LOCAL_DIR):
		buildModule(LOCAL_DIR, NAMESPACE_DIR, MODULE_DIR)
		config_module_filename = "{0}_{1}.xml".format(namespace, module)
		config_module_filename_path = os.path.join(ETC_MODULES_PATH, config_module_filename)
		config_file_module = open(config_module_filename_path, 'w+')
		config_file_module.write(namespace_module_xml)
		config_file_module.close()
		print ("Module created...")
	else:
		print ("Build local dir")
		#try:
		#	os.mkdir(LOCAL_DIR)
		#	buildModule(LOCAL_DIR, NAMESPACE_DIR, MODULE_DIR)
		#except Exception, e:
		#	raise 



