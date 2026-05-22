## Implementation of Vaccum Cleaner Problem using BFS
env={
    'A':'dirty',
    'D':'dirty',
    'C':'clean',
    'B':'clean'
}

items=env.items()
print('Initial Environment state:',env)

def vaccum_cleaner(env):
    for i in env:
        if env[i].casefold()=='dirty':
            env[i]='clean'
        elif env[i].casefold()=='clean':
            print(f'{i} is Already clean')


print('Cleaning the environment...')
vaccum_cleaner(env)
print('Final Environment state:',env)