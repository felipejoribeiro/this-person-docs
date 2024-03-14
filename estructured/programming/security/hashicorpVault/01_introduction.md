# Introduction to hashicorp
Hashicorp Vault is a tool created to solve the secret management problem.
Whe must manage credentials, that give authorization or authentication to a system, like user names and passwords, database credentials, api tokens, and tls certificates.

The normal way that this end up being managed is by leting then on all places, as plain text over your system, which isn't ideal. The chalenge is that the manager can't konw how has access to what and it's difficult to change these credentials too. This is the so called castle model.

Best benefits:
- So hashicorp tries to solve this by centralizing these credentials in one place and encrypt it's nice and safe. And it encrypts it in a way that who uses these credentials can't see it. And you can manage access to different keys in a user basis and you can audit who has acceced what.

- Other tool it has is dynamic secretes creation. It is important as various apps and database credentials can be created and distributed and if anything leaks than the leakage is contained in only one point of failure.

- Vault can make encryption as a service as well.. It creates a high level API with every encryption service you would expect, like encrypt, decrypt, verify and others... And the application can call these to its encryption endeavors.

## Pluggin capabilities
Vault is highly pluggable, it has numerous tools besides the core components that you can enable as needed. The central core deals with life cycle methods and if authorizations are being dealed properly. The extensions allows us to fit this infrastructure into our environment:
- Like the authentication backend. It allows Vault to allow clients to authenticate from different systems. The auth plugin can enable an ec2 instance, for example, to connect to our Vault, using an AWS-Vault plugin installed on said instance.
- The auditing plugin collects data about who took what in time and saves it. (splank, syslog, for example).
- Storage backend is the interface that integrates the Vault with a storage solution (mysql for example). The objective of these databases is to provide durable and resilient data storage and beeing highly available.
- Secrets backend enable the dynamic secrets functionalities and there are other plugins like database plugins that allow to dynamically manage mysql for example.


                                  ___________
                                 |           |
                                 |  storage  |
                                 |           |
                                  -----------
                                      |
                     _______      ___________       ___________
         ec2_VM --> |       |    |           |     |           |
         K8s -----> | Auth  | == |   core    | ==  |  secrets  |
                    |       |    |           |     |           |
                     -------      -----------       -----------
                                      |
                                  ___________
                                 |           |
                                 |   audit   |
                                 |           |
                                  -----------


In a broad deployment, we can run various Vault cores with shared backend. This provides scalability for even the most resourcefull infrastructures.


## Installing Vault
For installing Vault in debian based system you just need to issue the following commands:

```
curl -fsSL https://apt.releases.hashicorp.com/gpg | sudo apt-key add -
```

```
sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"
```

```
sudo apt-get update && sudo apt-get install vault
```

## The dev server
You can start experimenting with the development server initiating vault in your localhost with the following command:

```
vault server -dev
```

The dev server stores all data in memory and it shows you Unseal key and root token. Now with it running, configure your cli to access it:

```
export VAULT_ADDR='http://127.0.0.1:8200'
export "<Unseal Key>" > somewhere
export "<Root Token>" > somewhere
```


## writting secrets
When you send a secrete to vault, it wil encrypt it before sending to storage, so the database never sees it's true value and don't have the means to decrypt it without Vault.

To write a new secret to vault, you cas issue the following command:

```
vault kv put secret/hello foo=world
```
So you write a **pair** (foo=world) to a **path** (secret/hello).
You can write multiple pieces of data if you want:

```
vault kv put secret/hello foo=world hello=aloalo
```
This way has a problem, as your secret is stored on your **.bash_history**. For a better way of doing this, you can use files. Like the following `apikey.json` one:

```
{
	"key1": "AAaaBBccDDeeOTXzSMT1234BB_Z8JzG7JkSVxI",
	"key2": "AAaaBBccDDeeOTXzSMT1234BB_Z8JzG7JkSVxI"

}
```

And then, just issue the command like so:

```
vault kv put kv-v1/eng/apikey/Google @apikey.json
```

It is advised to ignore any vault commands to bash history, you can do that with the following command:

```
export HISTIGNORE="&:vault*"
```

## Getting a secret
Now that you have stored a secret you can get secrets with the following command:

```
vault kv get secret/hello
```

And it will return data about the secret on said path:

```
====== Metadata ======
Key              Value
---              -----
created_time     2020-09-02T21:41:17.568155Z
deletion_time    n/a
destroyed        false
version          2

===== Data =====
Key        Value
---        -----
excited    yes
foo        world
```

If you want a specific value you can use the `-field=` flag as follows:

```
vault kv get -field=excited secret/hello
```

You can get in json format as well with the `-format=json` option, it is interesting as you can pipe the result to `jq`:

```
vault kv get -format=json secret/hello | jq -r .data.data.excited
```

## Deleting a secret
To delete a key entry in your **Vault** you can make the following command:

```
vault kv delete secret/hello
```

So the data present on the specified path will be deleted.

## Secret engines
The path where these keys are stored is important. Until now we just created keys at **secret/** which is one of the default secret engines. You can check the ones you have installed with the following command:

```
vault secrets list
```

Notice that the first filed on the list is called **Path** and it is about where each secret engine is located. So by writting to **secret/hello** you are using the **kv** secret engine. And you can use others by changing the beggining of this path. You just can't use `sys/` as it is not intended for this.

You can enable a new secrets engine with the following command:

```
vault secrets enable -path=kv kv
```

Which is the same as:

```
vault secrets enable kv
```

As the default behavior is to make the path the same as the name of the secrets engine. You can check with the list command again.

Now you can store secrets with the `put` command just like before but wth the new path available:

```
vault kv put kv/hello target=world
```
You can list all keys that are available on each secrets engine with the following command:

```
vault secrets disable kv/
```

This will disable the path and disable all secrets and remove then from memory.

There are various secrets engines to install. Even `AWS` ones, or `database` ones. They can be used just as explained above, but under the hood these pluggins make all sorts of procedures unique for each secret storing method.

## Getting help
You can get help from any path with the following command (with secret/ as example):

```
vault path-help secret
```

So you will see a description and other important things. You can use it with even paths that don't exist. as the command just checks regular expressions on the path and don't is concerned with the real state of vault's virtual file system.

## Authentication
One way of authentication is with tokens, when you initiated the development vault server you received a root token, that has the root police which enables you to do anything. You can create a new one with the following command:

```
vault token create
```

By default the new token will inherit same policy as the parent one who created it, so, in this case, the root policy:

```
Key                  Value
---                  -----
token                s.iyNUhq8Ov4hIAx6snw5mB2nL
token_accessor       maMfHsZfwLB6fi18Zenj3qh6
token_duration       ∞
token_renewable      false
token_policies       ["root"]
identity_policies    []
policies             ["root"]
```

Now you can login in Vault with the given token. This can be done with the following command:

```
vault login s.iyNUhq8Ov4hIAx6snw5mB2nL
```

You can revoke tokens with the following command:

```
vault token revoke s.iyNUhq8Ov4hIAx6snw5mB2nL
```

## Github authentication
One can authenticate with **Vault** with github as well. So the user can provide his **Github** credentials and receive a Vault token in return.
This require aditional configuration so will elabore more on this later and use the token for now.


## Policies
Now that we can authenticate, we need a way of determining access for each user. This can be done through policies.

They are created on the **HCL** format and here goes an example:

```
# Dev servers have version 2 of KV secrets engine mounted by default, so will
# need these paths to grant permissions:
path "secret/data/*" {
  capabilities = ["create", "update"]
}

path "secret/data/foo" {
  capabilities = ["read"]
}
```

With this policy you can write any secret to `secret/data/` with the exception to `secret/data/foo` which only ready access is allowed. The default behavior is to deny access to everything.

There are two policies that comes preconfigured that are `default` and `root`. These can't be deleted.

You can write a new policy with the following command:

```
vault policy write my-policy ./my-policy.hcl
```

You can list all available policies with:

```
vault policy list
```

You can check how is each policy with the following command:

```
vault policy read my-policy
```

You can create a token with certain policy with the following method:

```
vault token create -policy=my-policy
```
And it wil give the default and the specified policy tho the new token.

You can check what policies your current active token has with the following command:

```
vault token lookup | grep policies
```

If the given policy doesn't give access to `sys` commands like `vault policy list` and `vault secrets list` will not work.


## Deploy for production
To deploy for development, first you must create a config file called **config.hcl** as follows:

```
storage "raft" {
  path    = "./vault/data"
  node_id = "node1"
}

listener "tcp" {
  address     = "127.0.0.1:8200"
  tls_disable = "true"
}

api_addr = "http://127.0.0.1:8200"
cluster_addr = "https://127.0.0.1:8201"
ui = true
```

The path for the storage must exist so you must create it with the `mkdir -p ./vault/data` command. Then you can initiate the server with the following instruction:

```
vault server -config=config.hcl
```

Then you can initialize it from another terminal with the following command:

```
export VAULT_ADDR='http://127.0.0.1:8200'

vault operator init
```

It will output the following credentials:

```
Unseal Key 1: 4jYbl2CBIv6SpkKj6Hos9iD32k5RfGkLzlosrrq/JgOm
Unseal Key 2: B05G1DRtfYckFV5BbdBvXq0wkK5HFqB9g2jcDmNfTQiS
Unseal Key 3: Arig0N9rN9ezkTRo7qTB7gsIZDaonOcc53EHo83F5chA
Unseal Key 4: 0cZE0C/gEk3YHaKjIWxhyyfs8REhqkRW/CSXTnmTilv+
Unseal Key 5: fYhZOseRgzxmJCmIqUdxEm9C3jB5Q27AowER9w4FC2Ck

Initial Root Token: s.KkNJYWF5g0pomcCLEmDdOVCW
```

With these you can unseal the vault and login as root.

Just install in your client pc the vault utility and configure it to comunicate with the chosen server instance. With these two ambient variables:

```
export VAULT_ADDR='http://IP...'
export VAULT_TOKEN='<roottoken>'
```

Then, you can generate new tokens with new policies as required.
