#!/usr/bin/python
# -*- coding: utf-8 -*-

from utils.alphabet import *

### Idea
## Keystream will be suppliable to anything requiring a passphrase (tabula recta) and possibly even keyword ciphers?
## In this sense the "autoclave" and "progressive" keystream options become easily available (via dropin) to any classes that need them

class KeyStream(object):
    def __init__(self, passphrase):
        """ We could accept a message ("autoclave element set"?) variable here and add that to the key stream as we go """
        self.passphrase = passphrase
        super(KeyStream, self).__init__()
    
    def __repr__(self):
        return repr(self.passphrase)
    
    def hotel_juliet(self, passphrase):
        """ Perform an action when the passphrase "rolls over" """
        return passphrase
    
    def stream(self, repeat=False):
        """ Generator """
        # Initialize our index
        idx = 0
        # Make a local copy to maintain sanity
        passphrase = self.passphrase
        # Iterate, iterate, iterate!
        #while repeat or idx < len(passphrase):
        while True:
            r = (yield passphrase[idx % len(passphrase)])
            if r is None:
                # If send() is not executed, advance to the next position
                idx += 1
            elif r >= 0:
                # Nonnegative send() values synchronize to a particular position
                idx = r % len(passphrase)
                # Override this!
                # passphrase = process_phrase(passphrase)
            else:
                # Negative send() values simply reset the stream index
                idx = 0
            if idx >= len(passphrase):
                # Advance the key (HOTEL JULIET?) and reset idx (presumably to zero)
                new_passphrase = self.hotel_juliet(passphrase)
                if new_passphrase != passphrase:
                    passphrase = new_passphrase
                else:
                    # Passphrase is not changed
                    break
                idx %= len(passphrase)

class RepeatedKeyStream(KeyStream):
    # Placeholder
    # Repeats the key
    # Standard Vigenere behavior
    pass

class AutoclaveKeyStream(KeyStream):
    # We could benefit from a message-char-in-common-with-alphabet generator here
    def __init__(self, passphrase, message, alphabet=None):
        """ We could accept a message ("autoclave element set"?) variable here and add that to the key stream as we go """
        self.passphrase = passphrase
        if not alphabet:
            alphabet = Alphabet()
        self.message_stream = (e for e in alphabet.common(message))
        return super(AutoclaveKeyStream, self).__init__(passphrase)
    
    def hotel_juliet(self, passphrase):
        # Pop a character off
        return passphrase + self.message_stream.next()

    # Appends plaintext to key
    # Standard autoclave behavior

class ProgressiveKeyStream(KeyStream):
    """ A keystream that advances its passphrase characters each time it is exhausted """
    def __init__(self, passphrase=None, alphabet=None):
        if not alphabet:
            alphabet = Alphabet()
        self.alphabet = alphabet
        return super(ProgressiveKeyStream, self).__init__(passphrase=passphrase)
    
    def advance(self, passphrase, by=1):
        # Experimental method to shift the letters in the passphrase
        o = []
        alphalen = len(self.alphabet)
        for e in passphrase:
            new_idx = self.alphabet.find(e) + by
            o.append(self.alphabet.element(new_idx % alphalen))
        return tuple(o)

    def stream(self):
        """ Generator """
        # Initialize our index
        idx = 0
        # Make a local copy to maintain sanity
        passphrase = self.passphrase
        pass_len = len(passphrase)
        # Iterate, iterate, iterate!
        while True:
            r = (yield passphrase[idx % pass_len])
            if idx >= pass_len:
                # Advance the key (HOTEL JULIET?) and reset idx (presumably to zero)
                idx %= pass_len
                passphrase = self.advance(passphrase)
            if r is None:
                # If send() is not executed, advance to the next position
                idx += 1
            elif r >= 0:
                # Nonnegative send() values synchronize to a particular position
                idx = r % pass_len
                passphrase = self.advance(self.passphrase, r // pass_len)
            else:
                # Negative send() values simply reset the stream index
                idx = 0

