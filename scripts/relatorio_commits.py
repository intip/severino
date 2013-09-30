#-*- coding:utf-8 -*-

from os import system
import sys

projetos = [
    '/cni-edital',
    '/cni-bancodemidia',
    '/cni-premio',
    '/cni-trainee',
]

if(len(sys.argv) < 2):
    raise Exception(
        """Por favor informe o diretorio onde estão as pastas dos projetos """)

root_dir = sys.argv[1]
since = sys.argv[2] if len(sys.argv) == 3 else '1.weeks'
report_file = "/tmp/relatorio_commits.txt"
git_log_command = \
    """git log --since=%s --pretty=format:'%%an, %%ar : %%s'"""

system('rm -f ' + report_file)
system('touch ' + report_file)

for i in projetos:
    path = root_dir + i
    cmd = git_log_command % since + ' >> ' + report_file
    system('echo "\\n\\n-------' + i + '-------\\n\\n" >> ' + report_file)
    system('cd ' + path + '; ' + cmd)



