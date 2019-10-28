# GreenGitHub
Python script that performs git operations. Schedule a daily run of this script to make your contribution breakdown a field of green (repository containing script must be public & device running script must have internet connection).

**Process:** <br/>
1) Discards all remote changes and pulls from master <br/>
2) Rewrites a text file with current datetime <br/>
3) Commits updated file to git repository <br/>

**Options:** <br/>
1) Make a single commit per run <br/>
2) Make a random number of commits per run <br/>

# Automation Options
**Windows Task Scheduler** <br/>
*-> Schedule a daily run with Windows Task Manager <br/>*

**Windows PowerShell** <br/>
*-> Schedule a daily run with a PowerShell script <br/>*

**Jenkins** <br/>
*-> Schedule a daily run with Jenkins <br/>*
