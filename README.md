Multi-tasking Test (Version 1.0)
--------------------------------

Last Modified: 25th May 2019

-   [Usage](#usage)
-   [Requirements](#requirements)
-   [Preference Setting](#setting)
-   [Task Description](#task)
-   [Output Description](#output)
-   [Behind the Scenes](#design)
-   [Creator](#creator)
-   [Reference & Acknowledgement](#reference)

### ❖ Usage

Please use *Terminal* to run this program. A Bash script file (i.e.,
*setup\_MTT.sh*) has been prepared for you to setup the experiment. \
 Note that the filepath can be easily obtained via drag & drop the
project folder to the Terminal window.

#### Example Usage:

\$ cd "Specify the filepath of the project folder here" \
 \$ sh setup\_MTT.sh

### ❖ Requirements

#### Platform

This program was primarily designed for and only tested on the *Mac OS
platform* (e.g., auto-set screen height and screen width).\
 Minimal modification of source code is needed if you plan to run this
program on the Windows platform. \
 (See comments in source code for details)

#### Python Version & Packages

Python version: 3.7.0 (Python 3.5 or greater is recommended to run this
program) \
 Please uncomment the "brew install" command in the bash script if you
only have older version. \
 **\>\> WHY:** Some relatively newer features of Python 3 were used in
this implementation:\
 **e.g.,** z = {\*\*x, \*\*y} syntax for merging dictionary requires
Python 3.5 or greater\
\
 External python packages were specified in *requirements.txt*. \
 A "pip install" command has already been included in the bash script.

### ❖ Preference Setting

You can further tailor this tool through preference setting (see setting
section / head of the source file).\
 This is a brief overview of the available options:

  -------------------- --------------------------------------------------------------------------- -----------------------------------------
  **Options**          **Descriptions**                                                            **Default**

  include\_practice    Whether a training session need to be scheduled before the formal session   True

  output\_path, etc.   You can change the output folder and names of output files.                 ./outputs/; \
                                                                                                   MTT\_log.csv (test results); \
                                                                                                   exp\_info\_log.csv (miscellaneous info)

  display\_time\       AKA: the max waiting time of subjects' response\                            3000 ms \<=\> 3 s
  (seconds)             i.e., the stimulus will disappear following a response or \                
                        following this setted display time in case no response was given           

  feedback\_time\      Duration of feedback message (for missed or incorrect response)\            500 ms \<=\> 0.5 s
  (seconds)             **[A SIDE NOTE]** \                                                        
                        if missed: "Time is up"; \                                                 
                        if incorrect: "That was the wrong key"                                     

  blank\_time\         AKA: rest time                                                              500 ms \<=\> 0.5 s
  (seconds)                                                                                        

  response\_key        - Press which keys to respond.\                                             left & right
                        - Designate which key as LEFT KEY & which as RIGHT KEY\                    
                        Normally, researchers use x & m, or left & right, etc.                     

  continue\_key        Press which keys to proceed                                                 space bar

  num\_trial\_prac     Number of trials in each block of practice session                          3

  num\_trial\_fml      Number of trials in each block of formal session \                          32
                       [!] Should be a multiple of 8                                               
  -------------------- --------------------------------------------------------------------------- -----------------------------------------

### ❖ Task Description

During the test, participant will see four types of figures presented at
different positions. \
 Subjects are asked to respond to the figures according to its shape,
filling, and position. \
 (see './img/instructions' folder or run a demo test for details)

#### Procedure

**Session**

**Block**

**Description**

Practice Session\
(Optional)

Shape-only Task

All figures will be presented in the *top* half of the box. \
\
 Subject only need to: \
 - judge whether it is a *diamond* (LEFT KEY) or a *square* (RIGHT KEY);
\
 - and press the corresponding key to respond.\
\
 Default number of trials: 3

Filling-only Task

All figures will be presented in the *bottom* half of the box. \
\
 Subject only need to: \
 - judge whether it has *2 dots* (LEFT KEY) or *3 dots* (RIGHT KEY); \
 - and press the corresponding key to respond.\
\
 Default number of trials: 3

Dual Task

The figures will be randomly presented in *either half of the box*. \
\
 Subject need to: \
 - judge its shape (TOP) or filling (BOTTOM) according to the position.
\
 - and press the corresponding key to respond.\
\
 Default number of trials: 3

Formal Session

Shape-only Task

Default number of trials: 32\
\
 i.e, \
 4 conditions \<= 2 possible shapes \* 2 possible fillings\
 As for the default trial number, each condition will repeat 8 (\<= 32 /
4) times

Filling-only Task

Default number of trials: 32\
\
 i.e, \
 4 conditions \<= 2 possible shapes \* 2 possible fillings\
 As for the default trial number, each condition will repeat 8 (\<= 32 /
4) times

Dual Task

Default number of trials: 32\
\
 i.e, \
 8 conditions \<= 2 possible shapes \* 2 possible fillings \* 2 possible
positions\
 As for the default trial number, each condition will repeat 4 (\<= 32 /
8) times

### ❖ Output Description

Two output files will be generated by this program (i.e., MTT\_log.csv
-\> test results; exp\_info\_log.csv -\> miscellaneous info).

-   The files will be written in *\* append mode \** (i.e., log for each
    participant will be written to the same file).
-   Subject ID, session No., block, and the trial No. can be used to
    identify each record.
-   The MTT\_log file will be updated on a per block basis, while the
    exp\_info\_log file will be updated on a per session basis.
-   The data generated by practice session won't be collected.

Brief description of the MTT\_log file:

**Output Fields**

**Description**

subject\_id

For identification purpose. Obtained from a dialogue box popped up at
the beginning of each session.

session\_no

block

shape\_task / filling\_task / dual\_task

TrialNumber

Trial No. in a block.

Shape

diamond / square

Filling

dots\_2 / dots\_3

Position

top / bottom

Target

shape / filling (i.e., whether subject need to judge the shape or
filling of a figure in a specific trial)

Answer

left\_key / right\_key\
\
 Note that the answer here are provided in terms of LEFT KEY or RIGHT
KEY: \
 - which means the program will evaluate participants' response properly
\
 - even if you designate other keys as the left/right key.

Congruent

1=congruent, 0=incongruent;\
\
 *congruent stimulus:* {diamond (left) + 2 dots (left)}, {square (right)
+ 3 dots (right)}\
 *incongruent stimulus:* {diamond (left) + 3 dots (right)}, {square
(right) + 2 dots (left)}

trial\_start

The moment the stimuli display; Format: timestamp

resp\_time

Response time (seconds). =\> [stimuli display ------- get response]\
 N/A if the participant fail to respond within the max waiting time (3s
by default)

response

left / right / no\_response\
\
 - record which key was pressed; \
 - only consider the first key press; \
 - response after the max waiting time (display time) will not be
accepted \
   (and actually a "Time is up" message will show up if there's no
response within the max waiting time);\
 - if you set 'x' as left key & 'm' as right key, the left & right in
this field will be replaced by x & m

accuracy

correct / wrong / missed (in case of no response)

other fields

Automatically generated by the TrialHandler class in the psychopy
package. Can be ignored.

Brief description of the exp\_info\_log file:

-   Start Info: subject ID, session No.
-   Preference Setting: include\_practice, timing-related settings,
    response keys, number of trials, etc.
-   Runtime Info: session\_start (timestamp), session\_end (timestamp)

### ❖ Behind the Scenes

#### Trial Sequencing

The trial sequence in each block is generated by the [TrialHandler
class](https://www.psychopy.org/api/data.html) in the psychopy package.\
 Specifically, the following parameters are used for trial sequencing:

-   trialList: see conditions.xlsx in the project folder
-   nReps: Repeat time of each condition. \
     By default, for practice session, nReps = 1; for formal session,
    nReps = num\_trial\_fml / number of conditions (4 or 8)
-   method: random. "‘random’ will result in a shuffle of the conditions
    on each repeat, \
     but all conditions occur once before the second repeat" cited from
    psychopy API

### ❖ Creator

  ----------------------- --------------------------------------------------------------------------
  **Team**                [CCMIR Lab @ HKU](http://ccmir.cite.hku.hk/) (Lab Director: Dr. Xiao Hu)
  **Major Contributor**   Li Fanjie
  ----------------------- --------------------------------------------------------------------------

### ❖ Reference & Acknowledgement

Stoet, G., O’Connor, D. B., Conner, M., & Laws, K. R. (2013). [Are women
better than men at
multi-tasking?](https://doi.org/10.1186/2050-7283-1-18). BMC Psychology,
1(1), 18.
