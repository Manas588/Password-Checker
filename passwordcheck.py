import requests
import hashlib
import sys

def request_api(query):
    url='https://api.pwnedpasswords.com/range/'+ query
    resp=requests.get(url)
    if resp.status_code !=200:
        raise RuntimeError(f"Error fetching : {resp.status_code},check api")
    return resp

def get_pass_leaks_count(hashes,hashes_to_check):
    hashes=(line.split(':')for line in hashes.text.splitlines())
    for h ,count in hashes:
      if h==hashes_to_check:
          return count
    return 0
def pwned_api_check(password):
    sha1pass=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_5,tail=sha1pass[:5],sha1pass[5:]
    resp=request_api(first_5)
    #print(resp)
    return get_pass_leaks_count(resp,tail)

def main(args):
    for password in args:
        count=pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times...you should probably change it!')
        else:print(f"{password} was not found. You are good to go")
    return "done"   


#main(sys.argv[1:])
def inputpass():
    a=[]
    while True:
         
         b=str(input("Enter a password to Check. Press ENTER to enter another password, enter \"END\" to stop :"))
         #print(b)
         if b=="END":
             break
         else:   
             a.append(b)
    #print(a)
    return main(a)         

inputpass()    