from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def main(args):
      my_seq = Seq("MKQHKAMIVALIVICITAVVAALVTRKDLCEVHIRTGQTEVAVF",
             IUPAC.protein)
      name = args.get("name", "stranger")
      greeting = "Hello test " + name + "!"
      print(greeting)
      return {"body": greeting}
  
