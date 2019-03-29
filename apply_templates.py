import os, re, sys
from jinja2 import Environment, FileSystemLoader, select_autoescape

"""
Apply Default Values to Jinja Templates


This script applies default values to 
nginx configuration templates in the 
conf.d_templates/ directory in order to
create hard-coded default configuration files.

The configuration templates are useful for Ansible,
but the hard-coded configuration files are useful
for everyone else.

All configuration files are for charlesreid1.com
docker pod, nginx, and realted infrastructure.
"""


# Where templates live
TEMPLATEDIR = 'conf.d_templates'

# Where rendered templates will go
OUTDIR = 'conf.d_new'

# Should existing files be overwritten
OVERWRITE = True

# Template variables
TV = {
        'server_name_default':  'charlesreid1.com',
        'server_name_gitea':    'git.charlesreid1.com',
        'server_name_files':    'files.charlesreid1.com',
        'server_name_pages':    'pages.charlesreid1.com',
        'server_name_hooks':    'hooks.charlesreid1.com',
        'server_name_bots':     'bots.charlesreid1.com',

        'pod_webhooks_server':  'localhost',

        'port_default':         '80',
        'port_gitea':           '80',
        'port_files':           '80',
        'port_pages':           '80',
        'port_hooks':           '80',
        'port_bots':            '80',

        'port_ssl_default':     '443',
        'port_ssl_gitea':       '443',
        'port_ssl_files':       '443',
        'port_ssl_pages':       '443',
        'port_ssl_hooks':       '443',
        'port_ssl_bots':        '443',
}



def apply_templates(template_dir, output_dir, template_vars, overwrite=False):
    """Apply the template variables to the template files
    to create rendered nginx configuration files.
    """

    if not os.path.exists(output_dir):
        msg = "Error: output dir %s does not exist!"%(output_dir)
        raise Exception(msg)

    if not os.path.exists(template_dir):
        msg = "Error: template dir %s does not exist!"%(output_dir)
        raise Exception(msg)

    # Jinja env
    env = Environment(loader=FileSystemLoader('conf.d_templates/'))

    # Render templates
    render_files = ['http.DOMAIN.conf', 'https.DOMAIN.conf', 'https.DOMAIN.subdomains.conf']
    template_files = [f+'.j2' for f in render_files]

    render_files = [re.sub('DOMAIN',template_vars['server_name_default'],s) for s in render_files]

    for rfile,tfile in zip(render_files,template_files):

        # Get rendered template content
        content = env.get_template(tfile).render(**template_vars)

        # Write to file
        dest = os.path.join(output_dir,rfile)
        if os.path.exists(dest) and overwrite is False:
            msg = "Error: template rendering destination %s already exists!"%(dest)
            raise Exception(msg)

        with open(dest,'w') as f:
            f.write(content)

    print("Rendered the following templates:%s\nOutput files:%s\n"%(
            "".join(["\n- "+os.path.join(template_dir,j) for j in template_files]),
            "".join(["\n- "+os.path.join(output_dir,j) for j in render_files])
    ))


if __name__=="__main__":
    apply_templates(TEMPLATEDIR,OUTDIR,TV,OVERWRITE)

