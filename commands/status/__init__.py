import urllib2
import logging
import json
import locale

def status_run_cmd(line, config):
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')
    logger = logging.getLogger('bot.cmd.status')
    logger.debug('Opening URL for status command')
    req = urllib2.Request(config['api_url'] + '&action=getpoolstatus&api_key=' + config['api_key'], headers={'User-Agent': 'Mozilla/5.0'})
    url = urllib2.urlopen(req)
    if url.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    logger.debug('Reading JSON data from response')
    jsonData = json.loads(url.read())
    reqpublic = urllib2.Request(config['api_url'] + '&action=public', headers={'User-Agent': 'Mozilla/5.0'})
    urlpublic = urllib2.urlopen(reqpublic)
    if urlpublic.getcode() != 200:
        logger.error('Request failed with http error: ' + str(url.getcode()))
        return False
    jsonPublicData = json.loads(urlpublic.read())
    strEfficiency = str(jsonData['getpoolstatus']['data']['efficiency']) + '%'
    strDifficulty = str(round(jsonData['getpoolstatus']['data']['networkdiff'], 3))
    strRoundEstimate = str(int(jsonData['getpoolstatus']['data']['estshares']))
    strCurrentRound = str(int(jsonPublicData['shares_this_round']))
    strHashrate = str(locale.format('%d', round(jsonPublicData['hashrate'], 2), grouping=True))
    strPoolLuck = str(round(jsonPublicData['shares_this_round'] / jsonData['getpoolstatus']['data']['estshares'] * 100, 2))
    strWorkers = str(jsonPublicData['workers'])
    logger.info('Completed command')
    return 'PRIVMSG ' + config['channel'] + ' :Pool Hashrate: ' + strHashrate + ' khash | Pool Efficiency: ' + strEfficiency + ' | Current difficulty: ' + strDifficulty + ' | Round Estimate: ' + strRoundEstimate + ' | Current Round: ' + strCurrentRound + ' | Round: ' + strPoolLuck + '% | Workers: ' + strWorkers
