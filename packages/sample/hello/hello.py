from data.data import OptionQuote, AmazonS3Source

def main(args):
      source = AmazonS3Source()
      greeting = str(source.last_date())
      print(greeting)
      return {"body": greeting}
  
