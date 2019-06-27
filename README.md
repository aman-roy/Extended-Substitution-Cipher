# Extended Substitution Cipher

Implementation of Extended substitution cipher. For more information read this - http://amanroy.me/extended-substitution-cipher

### Installation

$ pip install exsc

### Usage

For encryption:

>> from exsc import ExtendedSubCipher  
>> plaintext = "This is a test message."  
>> obj = ExtendedSubCipher("secret.323")  
>> ciphertext = obj.encrypt(plaintext)  
>> print(ciphertext)

For decryption:

>> from exsc import ExtendedSubCipher  
>> ciphertext = "lH@9w0vArR\~8L{%:0^=vc5c"
>> obj = ExtendedSubCipher("secret.323")  
>> plaintext = obj.decrypt(ciphertext)  
>> print(plaintext)


### Contributing

All contributions and suggestions are welcome!

1.  Fork it!
2.  Create your feature branch: git checkout -b my-new-feature
3.  Commit your changes: git commit -am 'Add some feature'
4.  Push to the branch: git push origin my-new-feature
5.  Submit a pull request

### Getting Help

If you have questions or need further guidance on using this template, please [file an issue](https://github.com/aman-roy/Extended-Substitution-Cipher/issues). I will do my best to respond to all issues in a timely manner.