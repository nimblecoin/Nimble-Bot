import urllib2
import logging
import json

def u_run_cmd(line, config):
    logger = logging.getLogger('bot.cmd.u')
    userNick = line.split(':')[2].split(' ')
    logger.debug(userNick)
    if len(userNick) == 2:
        userNick = userNick[1]
        req = urllib2.Request(config['api_url'] + '&action=getuserstatus&api_key=' + config['api_key'] + '&id=' + userNick, headers={'User-Agent': 'Mozilla/5.0'})
        url = urllib2.urlopen(req)
        if url.getcode() != 200:
            logger.error('Request failed with http error: ' + str(url.getcode()))
            return False
        jsonData = json.loads(url.read())
        logger.info('Completed command')
        return 'PRIVMSG ' + config['channel'] + ' :' + 'Username: ' + str(jsonData['getuserstatus']['data']['username']) + ' | Hashrate: ' + str(jsonData['getuserstatus']['data']['hashrate']) + ' kh/s' + ' | Shares Valid: ' + str(jsonData['getuserstatus']['data']['shares']['valid']) + ' | Shares Invalid: ' + str(jsonData['getuserstatus']['data']['shares']['invalid'])
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' : Unable to find username'
