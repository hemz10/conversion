import click

@click.command()
@click.option('--value','-v',help="Enter the value to be converted", required=True, prompt="Enter the value to be converted: \n")
def converter(value):

    near = 1000000000000000000000000
    result = int(value) / near
    print("Its " + str(result) + " near")

@click.command()
@click.option('--value','-v',help="Enter the value to be converted", required=True, prompt="Enter some number to be converted to near: \n")
def near(value):
    val=value.replace(".","")
    for _ in range(24):
        val = val + "0"
    while len(val) != 25:
        val = val[:-1]
    print(val)