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


config 9:00 Uhr

    myTwist.goal.twist.linear.x = np.clip(-dp[0],-1*10**(-3),1*10**(-3))

    if counter <300:
                kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
            else:
                kIBVS = 0.0001
            lin_index = 0

     if dp_mean_x_y < 5*10**(-7) or counter >1500: # 1*10**(-4)

    gefühlt beste config