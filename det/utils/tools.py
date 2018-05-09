import random
import string
import os
import yaml
from pkg_resources import resource_filename


import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import datetime


def as_flattened_list(iterable):
        """
        Return an iterable with one level flattened

        >>> as_flattened_list((('blue', 'red'), ('green', 'yellow', 'pink')))
        ['blue', 'red', 'green', 'yellow', 'pink']
        """
        return [e for i in iterable for e in i]


def validate_date(date_text):
        try:
                datetime.datetime.strptime(date_text, '%Y-%m-%d')
        except ValueError:
                raise ValueError("Incorrect data format, should be YYYY-MM-DD")


def validate_environment(env):
        allowed_env = ['d0', 't0', 'a7', 'p0']
        if env not in allowed_env:
                raise ValueError('Incorrect environment, should be in {}'.format(allowed_env))


def unique_in_list(seq):
        seen = set()
        seen_add = seen.add
        return [x for x in seq if not (x in seen or seen_add(x))]


def isa_group_separator(line):
        return line == '\n'


def send_mail(send_from,
              send_to,
              subject,
              text,
              files=None,
              server="127.0.0.1"):
    """Send email with possible attachment

    Args:
        - send_from(str): email address of the sender
        - send_to(str): email address of the receiver
        - subject(str): subject of the email
        - text(str): message string (content of the email)
        - files(list): list of files to be attached to the email
    """
    assert isinstance(send_to, list)
    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in files or []:
        with open(f, "rb") as fil:
            part = MIMEApplication(
                fil.read(),
                Name=basename(f)
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
        """Generate a random <size>-long string
        """
        return ''.join(random.choice(chars) for _ in range(size))


def find_txt_file_on_hdfs(hdfsfolder, machine, port=8020):
        """ Find list of txt files in HDFS folder on a local or remote machine

                Usage:

                $ find_txt_file_on_hdfs(hdfsfolder,"el3207",8020):

                Args:
                        - hdfsfolder(str): hdfs folder where to search for txt file
                        - machine(str): server/cluster on which the hdfs folder will be searched (name node)
                        - port(int): port (by default = 8020)

                Return:
                        - list of txt files
        """

        from snakebite.client import Client
        client = Client(machine, int(port), use_trash=False)
        txtfiles = list()
        for x in client.ls([os.path.join(hdfsfolder, '*.txt')]):
            txtfiles.append(x['path'])
        return(txtfiles)


def copy_hdfsfile_to_local(remotehdfsfile, localfile, machine, port=8020):
        """ Copy file from remote HDFS to local file which is returned

        """

        from snakebite.client import Client
        client = Client(machine, int(port), use_trash=False)
        c = list(client.copyToLocal([remotehdfsfile], localfile))
        return(localfile)


def mkdir_p(path):
        """Make directory tree, similar to make -p in unix
        """
        if not os.path.exists(path):
            try:
                os.makedirs(path)
            except OSError as exc:  # Python >2.5
                if exc.errno == errno.EEXIST and os.path.isdir(path):
                    pass
                else:
                    raise

def get_env_type(env):
    """ Reads the YAML file with the list of environments and returns the environment type
        
        For instance if env = 'd0' it will return as env_type 'DEV'
    """
    with open(resource_filename(__name__, os.path.join('..', 'templates', 'environment_types.yaml'))) as env_types_handle:
        env_types = yaml.load(env_types_handle)
        for k, v in env_types.items():
            if env in v:
                return k
    raise ValueError('Environment {} cannot be found'.format(env)) 
    return None
