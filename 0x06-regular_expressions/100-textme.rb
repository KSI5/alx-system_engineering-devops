#!/usr/bin/env ruby

file_path = ARGV[0]
if File.exist?(file_path)
  log_data = File.read(file_path)
  results = log_data.scan(/(?<=from:|to:|flags:)\+?\w+|\w+/).join(',')
  puts results
else
  puts "Error: Log file not found or inaccessible."
end
