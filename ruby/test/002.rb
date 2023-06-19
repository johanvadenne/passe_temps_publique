s = 'hello' 
puts s.sub( /[aeiou]/ , '*' ) # => "h*llo" 
puts s.gsub( /[aeiou]/ , '*' ) # => "h*ll*" 
puts s.gsub( /[aeiou]/ , '' ) # => "hll" 
puts s.sub( /ell/ , 'al' )    # => "halo" 
puts s.gsub( /xylly/ , '*' ) # => "bonjour" 
puts s.gsub( /&0/ , '*' ) # => "bonjour" 
puts 'THX1138'.gsub( /\d+/ , '00' ) # => "THX00"