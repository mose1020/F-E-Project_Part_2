# gute config

    alle Keypoints

    x,y 5mm

    myTwist.goal.twist.linear.x = np.clip(-dp[0],-1*10**(-3),1*10**(-3))

        if counter <300:
                    kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
                else:
                    kIBVS = 0.0001
                lin_index = 0

        if dp_mean_x_y < 5*10**(-7) or counter >3000: # 1*10**(-4)
 
# 2 config Keypoints select3ed and anderes Abruchkriterium

    selected Keypoints 

    x,y 5mm

    myTwist.goal.twist.linear.x = np.clip(-dp[0],-1*10**(-3),1*10**(-3))

        if counter <300:
                    kIBVS = 0.001 # gain default 0.001 # 0.000001 smallest possible value
                else:
                    kIBVS = 0.0001
                lin_index = 0

        if dp_mean_x_y < 2*10**(-6) or counter >3000: # 1*10**(-4)