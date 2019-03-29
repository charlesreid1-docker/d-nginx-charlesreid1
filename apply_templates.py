from jinja2 import Environment, PackageLoader, select_autoescape

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

TEMPLATEDIR = 'conf.d_templates'
OUTDIR = 'conf.d'

def apply_templates(template_dir, output_dir):

    if not os.path.exists(output_dir):
        msg = "Error: output dir %s does not exist!"%(output_dir)
        raise Exception(msg)

    if not os.path.exists(template_dir):
        msg = "Error: template dir %s does not exist!"%(output_dir)
        raise Exception(msg)

    # Jinja env
    e = Environment(loader=FileSystemLoader('conf.d_templates/'))

    #################
    # http template
    tvars = {
            'server_name_default':  'charlesreid1.com',
            'server_name_gitea':    'git.charlesreid1.com',
            'server_name_files':    'files.charlesreid1.com',
            'server_name_pages':    'pages.charlesreid1.com',
            'server_name_hooks':    'hooks.charlesreid1.com',
            'server_name_bots':     'bots.charlesreid1.com',
            'port_default':         '80',
            'port_gitea':           '80',
            'port_files':           '80',
            'port_pages':           '80',
            'port_hooks':           '80',
            'port_bots':            '80',
    }








    # Set default variable values
    template_variables = {
            'default_port' :        '80',
            'gitea_port' :          '3000',
    }

    # Render templates
    base_filename = 'playlists.html'
    template_filename = base_filename + '.j2'
    contents = env.get_template(template_filename).render(
            playlists_items = self.playlists,
            **template_variables
    )
    with open('%s/%s'%(output_dir,base_filename),'w') as f:
        f.write(contents)

