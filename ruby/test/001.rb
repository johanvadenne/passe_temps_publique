puts "bonjour"
bonjour = "bonjour tout le monde"
puts bonjour
puts "bonjour".reverse
puts "bonjour".length
puts "bonjour" * 5
puts 40 + 40
puts 40.to_s + 40.to_s
puts [12, 47, 35]
puts [12, 47, 35].max
puts [12, 47, 35].sort!
puts "bonjour tout le monde".gsub("tout le monde", "à tous")


bonjour = "bonjour tout le monde\nj'exécute du ruby"
puts bonjour.lines.reverse

puts bonjour.lines.reverse.join

books = {}
books["pivert"]  = :volatile
books["tigre"] = :félin
puts books