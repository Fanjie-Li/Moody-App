
		<div>
		<header>
			## Multi-tasking Test (Version 1.0)
		</header>
		Last Modified: 25th May 2019
		<nav>
			
				- [Usage](#usage)
				- [Requirements](#requirements)
				- [Preference Setting](#setting)
				- [Task Description](#task)
				- [Output Description](#output)
				- [Behind the Scenes](#design)
				- [Creator](#creator)
				- [Reference &amp; Acknowledgement](#reference)
			
		</nav>
		<article id="usage">
			### ❖ Usage
			 
				Please use <i>Terminal</i> to run this program. 
				A Bash script file (i.e., <i>setup_MTT.sh</i>) has been prepared for you to setup the experiment.   
&#10;				Note that the filepath can be easily obtained via drag &amp; drop the project folder to the Terminal window.
				#### Example Usage: 
			
			
				$ cd "Specify the filepath of the project folder here"   
&#10;				$ sh setup_MTT.sh
			
		</article>
		<article id="requirements">
			### ❖ Requirements
			#### Platform
			 
				This program was primarily designed for and only tested on the <i>Mac OS platform</i> (e.g., auto-set screen height and screen width).  
&#10;				Minimal modification of source code is needed if you plan to run this program on the Windows platform.   
&#10;				(See comments in source code for details)
			
			#### Python Version &amp; Packages
			 
				Python version: 3.7.0 (Python 3.5 or greater is recommended to run this program)   
&#10;				Please uncomment the "brew install" command in the bash script if you only have older version.   
&#10;				<b>&gt;&gt; WHY:</b> Some relatively newer features of Python 3 were used in this implementation:  
 &#10;				<span style="margin-left: 25px;">
					<b>e.g.,</b> z = {**x, **y} syntax for merging dictionary requires Python 3.5 or greater  
</span>  
&#10;				External python packages were specified in <i>requirements.txt</i>.   
&#10;				A "pip install" command has already been included in the bash script.
			
		</article>
		<article id="setting">
			### ❖ Preference Setting
			 
				You can further tailor this tool through preference setting (see setting section / head of the source file).  
&#10;				This is a brief overview of the available options:
			
			<table border="1px" width="875px">
				<tbody><tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;"><b>Options</b></td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;"><b>Descriptions</b></td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;"><b>Default</b></td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">include_practice</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Whether a training session need to be scheduled before the formal session</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">True</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">output_path, etc.</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">You can change the output folder and names of output files.</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">./outputs/;   
MTT_log.csv (test results);   
exp_info_log.csv (miscellaneous info)</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">display_time  
(seconds)</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						AKA: the max waiting time of subjects' response  

						i.e., the stimulus will disappear following a response or   

						following this setted display time in case no response was given
					</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">3000 ms &lt;=&gt; 3 s</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">feedback_time  
(seconds)</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						Duration of feedback message (for missed or incorrect response)  

						<b>[A SIDE NOTE]</b>   

						if missed: "Time is up";   

						if incorrect: "That was the wrong key"
					</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">500 ms &lt;=&gt; 0.5 s</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">blank_time  
(seconds)</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">AKA: rest time</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">500 ms &lt;=&gt; 0.5 s</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">response_key</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">- Press which keys to respond.  

											 - Designate which key as LEFT KEY &amp; which as RIGHT KEY  

											 Normally, researchers use x &amp; m, or left &amp; right, etc.</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">left &amp; right</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">continue_key</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Press which keys to proceed</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">space bar</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">num_trial_prac</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Number of trials in each block of practice session</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">3</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">num_trial_fml</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Number of trials in each block of formal session   
[!] Should be a multiple of 8</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">32</td>
				</tr>
			</tbody></table>
		</article>
		<article id="task">
			### ❖ Task Description
			 
				During the test, participant will see four types of figures presented at different positions.   
&#10;			    Subjects are asked to respond to the figures according to its shape, filling, and position.   
&#10;			    (see './img/instructions' folder or run a demo test for details)
			
			#### Procedure
			<table border="1px">
				<tbody><tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" width="140px"><b>Session</b></td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" width="140px"><b>Block</b></td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" width="550px"><b>Description</b></td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" rowspan="3">Practice Session  
(Optional)</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Shape-only Task</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						All figures will be presented in the <i>top</i> half of the box.   
<br>
						Subject only need to:   

						- judge whether it is a <i>diamond</i> (LEFT KEY) or a <i>square</i> (RIGHT KEY);   

						- and press the corresponding key to respond.  
<br>
						Default number of trials: 3
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Filling-only Task</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						All figures will be presented in the <i>bottom</i> half of the box.   
<br>
						Subject only need to:   

						- judge whether it has <i>2 dots</i> (LEFT KEY) or <i>3 dots</i> (RIGHT KEY);   

						- and press the corresponding key to respond.  
<br>
						Default number of trials: 3
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Dual Task</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						The figures will be randomly presented in <i>either half of the box</i>.   
<br>
						Subject need to:   

						- judge its shape (TOP) or filling (BOTTOM) according to the position.   

						- and press the corresponding key to respond.  
<br>
						Default number of trials: 3
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" rowspan="3">Formal Session</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Shape-only Task</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						Default number of trials: 32  
<br>
						i.e,   

						4 conditions &lt;= 2 possible shapes * 2 possible fillings  

						As for the default trial number, each condition will repeat 8 (&lt;= 32 / 4) times
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Filling-only Task</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						Default number of trials: 32  
<br>
						i.e,   

						4 conditions &lt;= 2 possible shapes * 2 possible fillings  

						As for the default trial number, each condition will repeat 8 (&lt;= 32 / 4) times
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Dual Task</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						Default number of trials: 32  
<br>
						i.e,   

						8 conditions &lt;= 2 possible shapes * 2 possible fillings * 2 possible positions  

						As for the default trial number, each condition will repeat 4 (&lt;= 32 / 8) times
					</td>
				</tr>
			</tbody></table>
		</article>
		<article id="output">
			### ❖ Output Description
			
				Two output files will be generated by this program (i.e., MTT_log.csv -&gt; test results; exp_info_log.csv -&gt; miscellaneous info).
				
				- 
    					The files will be written in <i>* append mode *</i> (i.e., log for each participant will be written to the same file).
    				
				- 
    					Subject ID, session No., block, and the trial No. can be used to identify each record.
    				
				- 
    					The MTT_log file will be updated on a per block basis, while the exp_info_log file will be updated on a per session basis.
    				
				- 
    					The data generated by practice session won't be collected.
    				
				
				Brief description of the MTT_log file:
			
			<table border="1px">
				<tbody><tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" width="115px"><b>Output Fields</b></td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" width="730px"><b>Description</b></td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">subject_id</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;" rowspan="2">For identification purpose. Obtained from a dialogue box popped up at the beginning of each session.</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">session_no</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">block</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">shape_task / filling_task / dual_task</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">TrialNumber</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Trial No. in a block.</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Shape</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">diamond / square</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Filling</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">dots_2 / dots_3</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Position</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">top / bottom</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Target</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">shape / filling (i.e., whether subject need to judge the shape or filling of a figure in a specific trial)</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Answer</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						left_key / right_key  
<br>
						Note that the answer here are provided in terms of LEFT KEY or RIGHT KEY:    

						- which means the program will evaluate participants' response properly   

						- even if you designate other keys as the left/right key.
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Congruent</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						1=congruent, 0=incongruent;  
<br>

						<i>congruent stimulus:</i> {diamond (left) + 2 dots (left)}, {square (right) + 3 dots (right)}  

						<i>incongruent stimulus:</i> {diamond (left) + 3 dots (right)}, {square (right) + 2 dots (left)}
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">trial_start</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">The moment the stimuli display; Format: timestamp</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">resp_time</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						Response time (seconds). =&gt; [stimuli display ------- get response]  

						N/A if the participant fail to respond within the max waiting time (3s by default)
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">response</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">
						left / right / no_response  
<br>
						- record which key was pressed;   

						- only consider the first key press;   

						- response after the max waiting time (display time) will not be accepted   

						&nbsp;&nbsp;(and  actually a "Time is up" message will show up if there's no response within the max waiting time);  

						- if you set 'x' as left key &amp; 'm' as right key, the left &amp; right in this field will be replaced by x &amp; m
					</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">accuracy</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">correct / wrong / missed (in case of no response)</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">other fields</td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Automatically generated by the TrialHandler class in the psychopy package. Can be ignored.</td>
				</tr>
			</tbody></table>
			
				Brief description of the exp_info_log file:
				
					- Start Info: subject ID, session No.
					- Preference Setting: include_practice, timing-related settings, response keys, number of trials, etc. 
					- Runtime Info: session_start (timestamp), session_end (timestamp)
				
			
		</article>
		<article id="design"> 
			### ❖ Behind the Scenes
			#### Trial Sequencing
			
				The trial sequence in each block is generated by the 
				[TrialHandler class](https://www.psychopy.org/api/data.html) 
				in the psychopy package.  
&#10;				Specifically, the following parameters are used for trial sequencing:
				
					- trialList: see conditions.xlsx in the project folder
					- nReps: Repeat time of each condition.   
    
    						By default, for practice session, nReps = 1; 
    						for formal session, nReps = num_trial_fml / number of conditions (4 or 8)
    					
					- method: random. "‘random’ will result in a shuffle of the conditions on each repeat,   
    
    						but all conditions occur once before the second repeat" cited from psychopy API
    					
				
			
		</article>
		<article id="creator">
			### ❖ Creator
			<table border="1px">
				<tbody><tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;"><b>Team</b></td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">[CCMIR Lab @ HKU](http://ccmir.cite.hku.hk/)&nbsp;(Lab Director: Dr. Xiao Hu)</td>
				</tr>
				<tr>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;"><b>Major Contributor</b></td>
					<td style="padding-top: 5px; padding-right: 5px; padding-bottom: 5px; padding-left: 5px;">Li Fanjie</td>
				</tr>
			</tbody></table>
		</article>
		<article id="reference">
			### ❖ Reference &amp; Acknowledgement
			Stoet, G., O’Connor, D. B., Conner, M., &amp; Laws, K. R. (2013). [Are women better than men at multi-tasking?](https://doi.org/10.1186/2050-7283-1-18). BMC Psychology, 1(1), 18.
		</article>
	</div>
	
