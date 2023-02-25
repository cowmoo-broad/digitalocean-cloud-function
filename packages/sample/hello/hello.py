def main(args):
      name = args.get("name", "stranger")
      greeting = "Hello test " + name + "!"
      print(greeting)
      return {"body": greeting}
  
