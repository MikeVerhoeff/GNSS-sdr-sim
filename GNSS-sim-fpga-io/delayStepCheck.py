#        tmp_n := n + itterNStep - delay_step; -- i am stearing on delay step, no feedback, will this work? need good external controle.
#        if tmp_n >= bufferNStep then -- tmp_n -> n?
#          n <= tmp_n - bufferNStep;
#          enable_modulation <= ENABLED;
#        else
#          n <= tmp_n;
#          enable_modulation <= DISABLED;
#        end if;

outputRate = 2600000
modulationRate = 1023000
subCycles = 100

itterNStep = subCycles * modulationRate # inputRate
bufferNStep = subCycles * outputRate

def step(n, delay_step):
    tmp_n = n + itterNStep - delay_step
    if tmp_n >= bufferNStep:
        n = tmp_n - bufferNStep
        return True, n
    else:
        n = tmp_n
        return False, n

def main():
    steps = [
        40976666, -27, 10, 11, 11, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 11, 12, 11, 11, 11, 11, 11, 11, 12, 11, 11, 11, 11, 12, 11, 11, 11, 11, 11, 12, 11, 11, 11, 11, 12, 11, 11, 11, 12, 11, 11, 11, 11, 12, 11, 11, 11, 12, 11, 11, 11, 12, 11, 11, 12, 11, 11, 11, 12, 11, 11, 12, 11, 11, 11, 12, 11, 11, 12
        
        ]
    targets = [
        17772963316834, 17772966180907, 17772969045511, 17772971911180, 17772974777646, 17772977644911, 17772980512973, 17772983381567, 17772986251225, 17772989121682, 17772991992936, 17772994864988, 17772997737572, 17773000611220, 17773003485666, 17773006360909, 17773009236951, 17773012113525, 17773014991162, 17773017869598, 17773020748831, 17773023628597, 17773026509426, 17773029391054, 17773032273479, 17773035156702, 17773038040457, 17773040925276, 17773043810893, 17773046697308, 17773049584255, 17773052472266, 17773055361075, 17773058250682, 17773061140820, 17773064032023, 17773066924023, 17773069816822, 17773072710152, 17773075604547, 17773078499739, 17773081395729, 17773084292251, 17773087189837, 17773090088222, 17773092987404, 17773095887118, 
17773098787895, 17773101689471, 17773104591845, 17773107494751, 17773110398720, 17773113303488, 17773116209053, 17773119115151, 17773122022312, 17773124930272, 17773127839029, 17773130748318, 17773133658671, 17773136569822, 17773139481505, 17773142394252, 17773145307797, 17773148222140, 17773151137015, 17773154052954, 17773156969690, 17773159887225, 17773162805292, 17773165724422, 17773168644351, 17773171564811, 17773174486335, 17773177408658, 17773180331778, 17773183255430, 17773186180146, 17773189105660, 17773192031706, 17773194958816, 17773197886724, 17773200815430, 17773203744667, 17773206674969, 17773209606069, 17773212537700, 17773215470396, 17773218403889, 17773221337914, 17773224273004, 17773227208891, 17773230145576, 17773233082793, 
17773236021074, 17773238960153, 17773241899764, 17773244840439, 17773247781912, 17773250723917
        ]
    predications = [
        0, 17772973250844, 17772966230844, 17772968830844, 17772971690844, 17772974550844, 17772977410844, 17772980270844, 17772983130844, 17772986250844, 17772989110844, 17772991970844, 17772994830844, 17772997690844, 17773000550855, 17773003410855, 17773006270855, 17773009130855, 17773011990855, 17773014850855, 17773017710855, 17773020570855, 17773023430855, 17773026290855, 17773029150855, 17773032270855, 17773035130855, 17773037990855, 17773040850855, 17773043710855, 17773046570855, 17773049430855, 17773052290855, 17773055150855, 17773058010855, 17773061130855, 17773063990855, 17773066850855, 17773069710855, 17773072570855, 17773075430855, 17773078290855, 17773081150855, 17773084270855, 17773087130855, 17773089990855, 17773092850855, 17773095710855, 17773098570855, 17773101430866, 17773104550866, 17773107410866, 17773110270866, 17773113130866, 17773115990866, 17773119110866, 17773121970866, 17773124830866, 17773127690866, 17773130550866, 17773133410866, 17773136530866, 17773139390866, 17773142250866, 17773145110866, 17773147970866, 17773151090866, 17773153950866, 17773156810866, 17773159670866, 17773162790866, 17773165650866, 17773168510866, 17773171370866, 17773174230866, 17773177350866, 17773180210866, 17773183070866, 17773185930866, 17773189050866, 17773191910866, 17773194770866, 17773197630866, 17773200750866, 17773203610877, 17773206470877, 17773209590877, 17773212450877, 17773215310877, 17773218170877, 17773221290877, 17773224150877, 17773227010877, 17773230130877, 17773232990877, 17773235850877, 17773238710877, 17773241830877, 17773244690877, 17773247550877

        ]
    u_pred = [
        433734, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260001, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 
260000, 260001, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260001, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 260000, 
260000, 260000, 260000, 260000, 260000, 260000
        ]

    print("start")

    n = 0
    i = 0
    delay = 0
    k = 0
    u=0
    while k < len(steps)-1:
        do_next, n = step(n, steps[k])
        delay += steps[k]
        u+=1
        if do_next:
            i+=1
            if i==(modulationRate//10):
                print(delay, targets[k], delay-targets[k], predications[k+1]-targets[k], u, u_pred[k])
                k+=1
                i=0
                u=0


if __name__ == "__main__":
    main()