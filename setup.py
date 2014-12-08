#!/usr/bin/env python
"""
/**********************************************************

    Organization    :AsymptopiaSoftware | Software@theLimit

    Website         :www.asymptopia.org

    Support         :www.asymptopia.org/forum

    Author          :Charles B. Cosse

    Email           :ccosse@asymptopia.org

    Copyright       :(C) 2006-2015 Asymptopia Software

    License         :GPLv3

***********************************************************/
"""
import os,sys
from setuptools import setup

APPNAME='TuxWordSmith'

setup(name='tuxwordsmith',
	version='0.8.1',
	description='pygame program that will teach your kids to add, subtract and multiply',
	url='http://www.asymptopia.org',
	author='Charles B. Cosse',
	author_email='ccosse@asymptopia.org',
	include_package_data=True,
	license='GPLV3',
	packages=[APPNAME],)

for sitepkgdir in sys.path:
	if sitepkgdir[-13:]=='site-packages':break

rm_path=os.path.join('/var/games/',APPNAME)
if os.path.exists(rm_path):
	cmd="rm -rf %s"%rm_path
	os.system(cmd)

rm_path=os.path.join(sitepkgdir,APPNAME)
if os.path.exists(rm_path):
	cmd="rm -rf %s"%rm_path
	print cmd
	os.system(cmd)

if len(sys.argv)>1 and sys.argv[1]=='uninstall':
	print 'application sucessfully removed.'
	sys.exit()
	
#Added 1/6/08 b/c Macs don't (apparantly) have /var/games by default (some linux distros may not, either)
if not os.path.exists('/var'):os.mkdir('/var')
if not os.path.exists('/var/games'):os.mkdir('/var/games')
if not os.path.exists('/var/games/TuxWordSmith'):os.mkdir('/var/games/TuxWordSmith')

path='/var/games/TuxWordSmith'

cmd="cp -r  xdxf Font README INSTALL CHANGES VERSION %s"%(path)
os.system(cmd)

cmd="chmod -R 755 /var/games/%s"%(APPNAME)
os.system(cmd)

cmd="cp .tws_config_master %s"%(path)
print cmd
os.system(cmd)

path=os.path.join(sitepkgdir,APPNAME)
if not os.path.exists(path):os.mkdir(path)

cmd="cp -r %s %s"%(APPNAME,sitepkgdir)
print cmd
os.system(cmd)

cmd="cp tuxwordsmith.py /usr/local/bin/tuxwordsmith"
print cmd
os.system(cmd)

cmd="chmod +x /usr/local/bin/%s"%('tuxwordsmith')
print cmd
os.system(cmd)

cmd="chmod -R 755 %s/%s"%(sitepkgdir,APPNAME)
print cmd
os.system(cmd)


##########################################################	
print '*********************************************'
print '*                                           *'
print '*           Setup Complete                  *'
print '*                                           *'
print '*  Run: /usr/local/bin/tuxwordsmith -help   *'
print '*                                           *'
print '*      Checkout more software at:           *'
print '*      http://www.asymptopia.org            *'
print '*                                           *'
print '*********************************************'
#!/usr/bin/env python
"""
/**********************************************************

    Organization    :AsymptopiaSoftware | Software@theLimit

    Website         :www.asymptopia.org

    Author          :Charles B. Cosse

    Email           :ccosse@gmail.com

    Copyright       :(C) 2006-2010 Asymptopia Software

    License         :GPLv3

***********************************************************/
"""
import os,sys
APPNAME='TuxWordSmith'

for sitepkgdir in sys.path:
	if sitepkgdir[-13:]=='site-packages':break

rm_path=os.path.join('/var/games/',APPNAME)
if os.path.exists(rm_path):
	cmd="rm -rf %s"%rm_path
	os.system(cmd)

rm_path=os.path.join(sitepkgdir,APPNAME)
if os.path.exists(rm_path):
	cmd="rm -rf %s"%rm_path
	print cmd
	os.system(cmd)

if len(sys.argv)>1 and sys.argv[1]=='uninstall':
	print 'application sucessfully removed.'
	sys.exit()
	
#Added 1/6/08 b/c Macs don't (apparantly) have /var/games by default (some linux distros may not, either)
if not os.path.exists('/var'):os.mkdir('/var')
if not os.path.exists('/var/games'):os.mkdir('/var/games')
if not os.path.exists('/var/games/TuxWordSmith'):os.mkdir('/var/games/TuxWordSmith')

path='/var/games/TuxWordSmith'

cmd="cp -r  Font %s"%(path)
os.system(cmd)

cmd="cp -r  xdxf %s"%(path)
os.system(cmd)

cmd="chmod -R 755 /var/games/%s"%(APPNAME)
os.system(cmd)

cmd="cp .tws_config_master %s"%(path)
print cmd
os.system(cmd)

path=os.path.join(sitepkgdir,APPNAME)
if not os.path.exists(path):os.mkdir(path)

cmd="cp -r %s %s"%(APPNAME,sitepkgdir)
print cmd
os.system(cmd)

cmd="cp tuxwordsmith.py /usr/local/bin/tuxwordsmith"
print cmd
os.system(cmd)

cmd="chmod +x /usr/local/bin/%s"%('tuxwordsmith')
print cmd
os.system(cmd)

cmd="chmod -R 755 %s/%s"%(sitepkgdir,APPNAME)
print cmd
os.system(cmd)


##########################################################	
print '*********************************************'
print '*                                           *'
print '*           Setup Complete                  *'
print '*                                           *'
print '*  Run: /usr/local/bin/tuxwordsmith -help   *'
print '*                                           *'
print '*      Checkout more software at:           *'
print '*      http://www.asymptopia.org            *'
print '*                                           *'
print '*********************************************'
