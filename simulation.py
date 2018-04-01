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
	coefMax = 1.0833333;
	powerMax = 1.14457831;
	weightMin = 0.85666;

	coef_ini = x1.Cells(9, utils.AlphabetPosition('G')).Value;
	power_ini = x1.Cells(10, utils.AlphabetPosition('G')).Value;
	weight_ini = x1.Cells(11, utils.AlphabetPosition('G')).Value;

	coef = x1.Cells(9, utils.AlphabetPosition('F'));
	power = x1.Cells(10, utils.AlphabetPosition('F'));
	weight = x1.Cells(11, utils.AlphabetPosition('F'));
	time = x1.Cells(18, utils.AlphabetPosition('H'));

	coef_it = coef.Value;
	power_it = power.Value;
	weight_it = weight.Value;

	improvementRate = 0.8;
	stepC = improvementRate * coefMax/100;
	stepP = improvementRate * powerMax/100;
	stepW = improvementRate * weightMin/100;

	utils.Print("Calculating ... \nIt will take a few seconds", 'red');

	i, j= 0, 0;
	optimalConfig = [coef_it, power_it, weight_it, time.Value, -1];
	while coef_it < coefMax:
		while power_it < powerMax:
			while weightMin < weight_it :

				j += 1;		
				remainingMoney = utils.Expensive(coef_it, power_it, weight_it);
				if remainingMoney < 0 :
					break;

				weight.Value = weight_it;
				power.Value = power_it;
				coef.Value = coef_it;

				if time.Value < optimalConfig[3]:
					i += 1;
					optimalConfig = [coef_it, power_it, weight_it, time.Value, remainingMoney];

				weight_it -= stepW;

			weight_it = weight_ini;
			power_it += stepP;

		weight_it = weight_ini;
		power_it = power_ini;
		coef_it += stepC;

	x1.Application.Quit();
	utils.Print("Done!", 'green');
	utils.Print("Number of cases tested: " + str(j), 'green');
	utils.Print("Optimal iterations: " + str(i), 'green');
	utils.WaitForSeconds(0.2);
	utils.PrintOptimal(optimalConfig);
	utils.WaitForSeconds(0.4);
	if (requestInput):
		utils.WaitForInput();
	return optimalConfig;
    