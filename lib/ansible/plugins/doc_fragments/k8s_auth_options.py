#
#  Copyright 2018 Red Hat | Ansible
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# Options for authenticating with the API.


class ModuleDocFragment(object):

    DOCUMENTATION = '''
options:
  host:
    description:
    - Provide a URL for accessing the API. Can also be specified via K8S_AUTH_HOST environment variable.
  api_key:
    description:
    - Token used to authenticate with the API. Can also be specified via K8S_AUTH_API_KEY environment variable.
  kubeconfig:
    description:
    - Path to an existing Kubernetes config file. If not provided, and no other connection
      options are provided, the openshift client will attempt to load the default
      configuration file from I(~/.kube/config.json). Can also be specified via K8S_AUTH_KUBECONFIG environment
      variable.
  context:
    description:
    - The name of a context found in the config file. Can also be specified via K8S_AUTH_CONTEXT environment variable.
  username:
    description:
    - Provide a username for authenticating with the API. Can also be specified via K8S_AUTH_USERNAME environment
      variable.
    - Please note that this only works with clusters configured to use HTTP Basic Auth. If your cluster has a
      different form of authentication (e.g. OAuth2 in OpenShift), this option will not work as expected and you
      should look into the C(k8s_auth) module, as that might do what you need.
  password:
    description:
    - Provide a password for authenticating with the API. Can also be specified via K8S_AUTH_PASSWORD environment
      variable.
    - Please read the description of the C(username) option for a discussion of when this option is applicable.
  cert_file:
    description:
    - Path to a certificate used to authenticate with the API. Can also be specified via K8S_AUTH_CERT_FILE environment
      variable.
  key_file:
    description:
    - Path to a key file used to authenticate with the API. Can also be specified via K8S_AUTH_KEY_FILE environment
      variable.
  ssl_ca_cert:
    description:
    - Path to a CA certificate used to authenticate with the API. The full certificate chain must be provided to
      avoid certificate validation errors. Can also be specified via K8S_AUTH_SSL_CA_CERT environment variable.
  verify_ssl:
    description:
    - "Whether or not to verify the API server's SSL certificates. Can also be specified via K8S_AUTH_VERIFY_SSL
      environment variable."
    type: bool

notes:
  - "The OpenShift Python client wraps the K8s Python client, providing full access to
    all of the APIS and models available on both platforms. For API version details and
    additional information visit https://github.com/openshift/openshift-restclient-python"
  - "To avoid SSL certificate validation errors when C(verify_ssl) is I(True), the full
    certificate chain for the API server must be provided via C(ssl_ca_cert) or in the
    kubeconfig file."
'''
