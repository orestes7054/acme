## Acme Exersice IOET May 2022
Orestes Olivera Marrero
### Architecture
The main function of the program is to compute the total payment amount for the employees of the ACME Company. The input is a .txt file with this format:
<pre>RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00</pre>
**The output:**
<pre>The amount to pay RENE is: 215 USD</pre>
<body>
	<h1>Directory Tree</h1><p>
	<a href="./">./</a><br>
	├── <a href=".//ACME/">ACME</a><br>
	│   ├── <a href=".//ACME/acme.txt">acme.txt</a><br>
	│   ├── <a href=".//ACME/errors.py">errors.py</a><br>
	│   ├── <a href=".//ACME/__init__.py">__init__.py</a><br>
	│   ├── <a href=".//ACME/__main__.py">__main__.py</a><br>
	│   ├── <a href=".//ACME/payment_class.py">payment_class.py</a><br>
	│   ├── <a href=".//ACME/payment.json">payment.json</a><br>
	│   └── <a href=".//ACME/utils.py">utils.py</a><br>
	├── <a href=".//acme_employee_payment_roll.txt">acme_employee_payment_roll.txt</a><br>
	├── <a href=".//LICENSE">LICENSE</a><br>
	├── <a href=".//README.md">README.md</a><br>
	├── <a href=".//result.html">result.html</a><br>
	├── <a href=".//setup.py">setup.py</a><br>
	└── <a href=".//test/">test</a><br>
	&nbsp;&nbsp;&nbsp; ├── <a href=".//test/data/">data</a><br>
	&nbsp;&nbsp;&nbsp; │   ├── <a href=".//test/data/empty_file.txt">empty_file.txt</a><br>
	&nbsp;&nbsp;&nbsp; │   ├── <a href=".//test/data/test_acme_five_employees.txt">test_acme_five_employees.txt</a><br>
	&nbsp;&nbsp;&nbsp; │   ├── <a href=".//test/data/test_acme.txt">test_acme.txt</a><br>
	&nbsp;&nbsp;&nbsp; │   └── <a href=".//test/data/wrong_format.jpg">wrong_format.jpg</a><br>
	&nbsp;&nbsp;&nbsp; ├── <a href=".//test/__init__.py">__init__.py</a><br>
	&nbsp;&nbsp;&nbsp; └── <a href=".//test/test_acme.py">test_acme.py</a><br>
	<br><br>
	</p>
	<p>

5 directories, 25 files
	<br><br>
	</p>
	<hr>
</body>

Sorted by hierarchy the ACME file contains the core operations. In **payment_class.py** is the main class that make the computation. In **utils.py** are the function to check the user's input, clear the data and transform text to datetime objects. In **errors.py** are the classes for erorrs. *I tried to keep the project as simple as posible and don't abuse the Classes' use; avoiding the re-calling of simple functions*. The **test** folder includes all the neccesary elements to test the code. The **setup.py** is use to create all the neccesaries elements to make a module of every folder with no problems. [Related to setup.py](https://xkcd.com/353/) 
<p>In the <b>utils.py</b> the functions are concatenate, this is a practice I inherit from <a href="https://docs.microsoft.com/en-us/office/vba/library-reference/concepts/getting-started-with-vba-in-office">VBA</a> where you usually call a function from a function and run the program consecutively, this is also use in <a href="https://www.google.com/script/start/">Google Apps Script</a>. The days and payment information is in the payment.json file; the AcmeEmployee class reads this file and obtain the data.
	
![ACME](https://user-images.githubusercontent.com/56367486/168681520-803e911a-0576-4711-a833-125dba40cea0.PNG)
	
	
### Installation via PIP
	pip install acme-ioet-orestes
<p>Then use terminal with:</p>
<p>For instructions</p>
<pre>ACME -h</pre>
<p>To see and example:</p>
<pre>ACME -example</pre>
<p>To use the program</p>
<pre>ACME &#60path to the .txt file&#62</pre>
<p>If you want to save a copy of the output:</p>
<pre>ACME -sc &#60path to the .txt file&#62</pre>

### Manual Installation
<pre>git clone https://github.com/orestes7054/acme.git</pre>
<pre>cd acme</pre>
<pre>pip install .</pre>
<p>For instructions</p>
<pre>python ACME -h</pre>
<p>To see and example:</p>
<pre>python ACME -example</pre>
<p>To use the program</p>
<pre>python ACME &#60path to the .txt file&#62</pre>
<p>If you want to save a copy of the output:</p>
<pre>python ACME -sc &#60path to the .txt file&#62</pre>

### Test
<pre>git clone https://github.com/orestes7054/acme.git</pre>
<pre>cd acme</pre>
<pre>pip install .</pre>
<pre>python -m unittest -v</pre>

### Assumptions
1. The employees can not make portion of hour, they have to submit a complete hour.
2. An employee can not make just one day of work, the program will not read a line like this: RENE=MO10:00-15:00. If this assumptions is not correct, to change this and read just one day we need to change the **check_line** function regex.

* * *

<ins>NOTE</ins>: The use of the command <pip install .> is to avoid dependencies problems. For some version of linux (ubuntu 18.04 for example) the use of <python3 setup.py install> is not recommended. 
For use is recommended the pip via install.
	

