require 'releasy'

Releasy::Project.new do
  name "MonApplication"
  version "1.0.0"
  file "test_1.rb"

  add_build :executable
end
