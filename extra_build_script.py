Import("env")

def cmsis_build_helper(node):
    return env.Object(
        target='startup_stm32h750xx.o', source= 'startup_stm32h750xx.c'
        )

print("running extra script!!!!!!!!")    
# env.AddBuildMiddleware(cmsis_build_helper)