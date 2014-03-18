import urllib2
import logging
import json

def last_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.last')
    logger.debug('Running command cmd.last')
    req = urllib2.Request(config['api_url'] + '&action=getblocksfound&api_key=' + config['api_key'] + '&limit=1', headers={'User-Agent': 'Mozilla/5.0'})
    url = urllib2.urlopen(req)
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    jsonData = json.loads(url.read())
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :' + 'Last Block: #' + str(jsonData['getblocksfound']['data'][0]['height']) + ' | Amount: ' + str(jsonData['getblocksfound']['data'][0]['amount']) + ' | Shares: ' + str(jsonData['getblocksfound']['data'][0]['shares']) + ' | Confirmations: ' + str(jsonData['getblocksfound']['data'][0]['confirmations']) + ' | Found by: ' + str(jsonData['getblocksfound']['data'][0]['finder'])
