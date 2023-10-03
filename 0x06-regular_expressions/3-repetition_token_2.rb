#!/usr/bin/env ruby
# matching hbtn, hbttn, hbtttn, hbttttn

puts ARGV[0].scan(/hbt+n/).join
