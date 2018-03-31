import utils, win32com.client

def Run(track):
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

	stepC = 0.05 * coefMax;
	stepP = 0.05 * powerMax;
	stepW = 0.03 * weightMin;

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
					#print ("\nA new optimal has been found");
					#utils.PrintOptimal(optimalConfig);

				weight.Value -= stepW;

			weight.Value = weight_ini;
			power.Value +=stepP;

		weight.Value = weight_ini;
		power.Value = power_ini;
		coef.Value += stepC;

	x1.Application.Quit();
	utils.Print("Done!", 'green');
	utils.PrintOptimal(optimalConfig);
	utils.WaitForSeconds(2);
	return optimalConfig;
	#print("Number of values founded", i);
    