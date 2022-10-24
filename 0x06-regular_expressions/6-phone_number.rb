#!/usr/bin/env ruby
# matching ten digits number

puts ARGV[0].scan(/^[0-9]{10}$/).join
