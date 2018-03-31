# -*- coding: utf-8 -*-
#title           :  simulation.py
#description     :  Calculate the best values for the parameters of a race car
#author          :  Juan Ortiz
#date            :  30 March 2018
#version         :  0.1
#python_version  :  2.7.14
#=======================================================================

import utils, win32com.client

def Run(track, requestInput=True):
	utils.msgCool(track)
	utils.Print("Initializing the simulator ...", 'green');
	path = track+'.xlsx';
	x1 = win32com.client.DispatchEx("Excel.Application");
	wb1 = x1.Workbooks.Open(path);
	x1.DisplayAlerts = False;

	# Constraints
	powerMax = 14.457831;
	coefMax = 8.33333;
	weightMin = 0.85666;

	coef_ini = x1.Cells(9, utils.AlphabetPosition('G')).Value;
	power_ini = x1.Cells(10, utils.AlphabetPosition('G')).Value;
	weight_ini = x1.Cells(11, utils.AlphabetPosition('G')).Value;

	coef = x1.Cells(9, utils.AlphabetPosition('F'));
	power = x1.Cells(10, utils.AlphabetPosition('F'));
	weight = x1.Cells(11, utils.AlphabetPosition('F'));
	time = x1.Cells(18, utils.AlphabetPosition('H'));

	improvementRate = 1;
	stepC = improvementRate * coefMax/100;
	stepP = improvementRate * powerMax/100;
	stepW = improvementRate * weightMin/100;

	print("Calculating ...");

	i = 0;
	optimalConfig = [coef.Value, power.Value, weight.Value, time.Value];
	while coef.Value < coefMax:
		while power.Value < powerMax:
			while weightMin < weight.Value :

				if not utils.feasibility(coef.Value, power.Value, weight.Value) :
					break;

				if time.Value < optimalConfig[3]:
					i += 1;
					optimalConfig = [coef.Value, power.Value, weight.Value, time.Value];

				weight.Value -= stepW;

			weight.Value = weight_ini;
			power.Value +=stepP;

		weight.Value = weight_ini;
		power.Value = power_ini;
		coef.Value += stepC;

	x1.Application.Quit();
	utils.Print("Done!", 'green');
	utils.WaitForSeconds(0.2);
	utils.PrintOptimal(optimalConfig);
	utils.WaitForSeconds(0.4);
	if (requestInput):
		utils.WaitForInput();
	return optimalConfig;
    