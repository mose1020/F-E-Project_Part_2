Immer so lassen:

z = 100 #höhe roboter
Speed = 100%
z =0.293 #Regler Abstand zur Kamera


1 config 

 # calculate the twist with the ibvs controller
            if counter <200:
                kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
            else:
                kIBVS = 0.0001
            lin_index = 0

if dp_mean_x_y < 5*10**(-6) or counter >1500: # 1*10**(-4)

myTwist.goal.twist.linear.x = np.clip(-dp[0],-1*10**(-2),1*10**(-2)) #geklippt auf 10**(-2)


zu früh abgebrochen

2 config

 # calculate the twist with the ibvs controller
            if counter <200:
                kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
            else:
                kIBVS = 0.0001
            lin_index = 0

if dp_mean_x_y < 2*10**(-6) or counter >1500: # 1*10**(-4)

myTwist.goal.twist.linear.x = np.clip(-dp[0],-1*10**(-2),1*10**(-2)) #geklippt auf 10**(-2)


3 config 

      # calculate the twist with the ibvs controller
            if counter <200:
                kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
            else:
                kIBVS = 0.0002
            lin_index = 0

    if dp_mean_x_y < 2*10**(-6) or counter >1000: # 1*10**(-4)

    myTwist.goal.twist.linear.x = np.clip(-dp[0],-5*10**(-3),5*10**(-3))


    config

     # calculate the twist with the ibvs controller
            if counter <200:
                kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
            else:
                kIBVS = 0.0003
            lin_index = 0

    if dp_mean_x_y < 2*10**(-6) or counter >1500: # 1*10**(-4)


    config

     # calculate the twist with the ibvs controller
            if counter <200:
                kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
            else:
                kIBVS = 0.0005
            lin_index = 0

    if dp_mean_x_y < 5*10**(-7) or counter >1000: # 1*10**(-4)

     myTwist.goal.twist.linear.x = np.clip(-dp[0],-5*10**(-3),5*10**(-3))

config 9:00 Uhr

    myTwist.goal.twist.linear.x = np.clip(-dp[0],-1*10**(-3),1*10**(-3))

    if counter <300:
                kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
            else:
                kIBVS = 0.0001
            lin_index = 0

     if dp_mean_x_y < 5*10**(-7) or counter >1000: # 1*10**(-4)

    gefühlt beste config

    Startpose des Roboters:  [0.10318030708875578, -0.4875586602198753, 0.09999896002911018, -0.7208733434282958, -0.693021200309768, -0.0018210001596882066, 0.007740969844747243]


    Endpose des Roboters:  [0.05561771165462145, -0.538955259919083, 0.10000206842211751, -0.7218742840046996, -0.6919786119796153, -0.0018360060105141636, 0.0077296660598686825]


    Zielpose des Roboters [0.05318934002738384, -0.5375691858099181, 0.10001297264803716, -0.7208680959367131, -0.693026898724365, -0.0018095566026939867, 0.0077221376553715994]


    Differenz zwischen Starpose und Zielpose:  [0.04999096706137194, 0.050010525590042765, -1.401261892697292e-05, -5.247491582704988e-06, 5.698414596966295e-06, -1.1443556994219931e-05, 1.8832189375643515e-05]


    Differenz zwischen Endpose und Zielpose:  [0.0024283716272376077, -0.0013860741091649142, -1.0904225919650123e-05, -0.0010061880679864688, 0.0010482867447496602, -2.6449407820176938e-05, 7.528404497083099e-06]


    Regeltakt:  7.526315789473684


    Anzahl der lineare abhängigen Iterationen:  3


config 2 8.August

    myTwist.goal.twist.linear.x = np.clip(-dp[0],-1*10**(-3),1*10**(-3))

    if counter <300:
                kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
            else:
                kIBVS = 0.0001
            lin_index = 0

     if dp_mean_x_y < 5*10**(-7) or counter >1500: # 1*10**(-4)


    [get_image_data] Done saving camera image
    Testen mit Graustufen-Bildern
    checkpoint loaded.
    [ 1.27830518e-04  1.10667819e-04  1.05036799e-06 -9.76827387e-09
    -5.86425696e-10  3.50221219e-07]
    Iteration number:  1500


    Startpose des Roboters:  [0.10319505917623292, -0.48757994447055475, 0.10002112988802508, -0.7208679232957681, -0.6930272250745418, -0.0018038225673764339, 0.007710297845903755]


    Endpose des Roboters:  [0.05342769951808426, -0.5388879804307016, 0.10001604555670573, -0.7216652689874662, -0.6921967126366136, -0.00181852457434113, 0.0077229217713313345]


    Zielpose des Roboters [0.05318934002738384, -0.5375691858099181, 0.10001297264803716, -0.7208680959367131, -0.693026898724365, -0.0018095566026939867, 0.0077221376553715994]


    Differenz zwischen Starpose und Zielpose:  [0.05000571914884908, 0.04998924133936333, 8.157239987927056e-06, 1.726409449842592e-07, -3.263501768824284e-07, 5.734035317552779e-06, -1.1839809467844783e-05]


    Differenz zwischen Endpose und Zielpose:  [0.00023835949070041829, -0.0013187946207835477, 3.0729086685776785e-06, -0.0007971730507531083, 0.0008301860877513167, -8.967971647143302e-06, 7.841159597350711e-07]


    Regeltakt:  7.505


    Anzahl der lineare abhängigen Iterationen:  14

config 3 8 August

    myTwist.goal.twist.linear.x = np.clip(-dp[0],-1*10**(-3),1*10**(-3))

    if counter <300:
                kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
            else:
                kIBVS = 0.0001
            lin_index = 0

     if dp_mean_x_y < 5*10**(-7) or counter >3000: # 1*10**(-4)


     [get_image_data] Done saving camera image
    Testen mit Graustufen-Bildern
    checkpoint loaded.
    [ 3.55765432e-05 -3.26320508e-05  7.51954653e-07 -1.09896283e-08
    -1.68340206e-09  1.74761182e-06]
    Iteration number:  3000


    Startpose des Roboters:  [0.10317529410095365, -0.4875588625208048, 0.10000076113517997, -0.7208622567751845, -0.6930326722573887, -0.0018073488590205182, 0.007749543913848803]


    Endpose des Roboters:  [0.0483441430192738, -0.5388154200482715, 0.1000052726146562, -0.7216749142372753, -0.6921865999988706, -0.001836526978769652, 0.0077237368728778405]


    Zielpose des Roboters [0.05318934002738384, -0.5375691858099181, 0.10001297264803716, -0.7208680959367131, -0.693026898724365, -0.0018095566026939867, 0.0077221376553715994]


    Differenz zwischen Starpose und Zielpose:  [0.04998595407356981, 0.050010323289113257, -1.2211512857185358e-05, 5.839161528631287e-06, -5.7735330237784765e-06, 2.207743673468456e-06, 2.7406258477203835e-05]


    Differenz zwischen Endpose und Zielpose:  [-0.004845197008110043, -0.0012462342383534608, -7.700033380964033e-06, -0.0008068183005621732, 0.0008402987254944039, -2.697037607566526e-05, 1.5992175062410144e-06]


    Regeltakt:  7.5024999999999995


    Anzahl der lineare abhängigen Iterationen:  127


    