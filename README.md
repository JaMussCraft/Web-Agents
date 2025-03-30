# Web-Agents
Research and experiments on web-based agents research.

### Environment variables
```bash
export AGENTLAB_EXP_ROOT=./experiment-results
export OPENAI_API_KEY=<your openai api key> # if openai models are used
```


## MiniWob

## WebArena
Commands for running dockers:
```bash
docker exec shopping /var/www/magento2/bin/magento setup:store-config:set --base-url="http://ec2-23-21-14-136.compute-1.amazonaws.com:7770" # no trailing /
docker exec shopping mysql -u magentouser -pMyPassword magentodb -e  'UPDATE core_config_data SET value="http://ec2-23-21-14-136.compute-1.amazonaws.com:7770/" WHERE path = "web/secure/base_url";'
# remove the requirement to reset password
docker exec shopping_admin php /var/www/magento2/bin/magento config:set admin/security/password_is_forced 0
docker exec shopping_admin php /var/www/magento2/bin/magento config:set admin/security/password_lifetime 0
docker exec shopping /var/www/magento2/bin/magento cache:flush

docker exec shopping_admin /var/www/magento2/bin/magento setup:store-config:set --base-url="http://ec2-23-21-14-136.compute-1.amazonaws.com:7780"
docker exec shopping_admin mysql -u magentouser -pMyPassword magentodb -e  'UPDATE core_config_data SET value="http://ec2-23-21-14-136.compute-1.amazonaws.com:7780/" WHERE path = "web/secure/base_url";'
docker exec shopping_admin /var/www/magento2/bin/magento cache:flush

docker exec gitlab sed -i "s|^external_url.*|external_url 'http://ec2-23-21-14-136.compute-1.amazonaws.com:8023'|" /etc/gitlab/gitlab.rb
docker exec gitlab gitlab-ctl reconfigure
```
* Fatal errors with last gitlab commands... couldn't fix... but gitlab seems to be functional...

### Environment variables
```bash
BASE_URL="http://ec2-23-21-14-136.compute-1.amazonaws.com"

# webarena environment variables (change ports as needed)
export WA_SHOPPING="$BASE_URL:7770/"
export WA_SHOPPING_ADMIN="$BASE_URL:7780/admin"
export WA_REDDIT="$BASE_URL:9999"
export WA_GITLAB="$BASE_URL:8023"
export WA_WIKIPEDIA="$BASE_URL:8888/wikipedia_en_all_maxi_2022-05/A/User:The_other_Kiwix_guy/Landing"
export WA_MAP="$BASE_URL:3000"
export WA_HOMEPAGE="$BASE_URL:80"
```

## WorkArena

### Environment variables
```bash
export SNOW_INSTANCE_URL=https://dev276413.service-now.com
export SNOW_INSTANCE_UNAME=admin
export SNOW_INSTANCE_PWD=JL%\!edhEm13W
```

## WebLinx

### Environment variables
```bash
export BROWSERGYM_WEBLINX_CACHE_DIR=./bg_wl_data
```

### Make sure project contains directory "bg_wl_data" with [this dataset](https://huggingface.co/datasets/McGill-NLP/weblinx-browsergym)


## AssistantBench

* Just run custom_experiment.py with proper setup

## VisualWebArena

* AMI not available anymore... could try setting websites manually...
* Haven't explored paper