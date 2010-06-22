require 'rake'
require 'spec/rake/spectask'

task :deploy => ['services:twitter', :jekyll]

namespace :services do
  desc 'Generate Twitter include file'
  task :twitter do
    ruby File.join(File.dirname(__FILE__), 'scripts', 'twitter.rb')
  end

  desc 'Generate Flickr include file'
  task :flickr do
    ruby File.join(File.dirname(__FILE__), 'scripts', 'flickr.rb')
  end

  desc 'Generate Last.fm include file'
  task :lastfm do
    ruby File.join(File.dirname(__FILE__), 'scripts', 'lastfm.rb')
  end

  desc 'Send ping request to Pingomatic'
  task :pingomatic do
    ruby File.join(File.dirname(__FILE__), 'scripts', 'pingomatic.rb')
  end
end

file '_site/index.html' => FileList['source/_includes/*.html'] do
  sh '/opt/rubyee/bin/jekyll'
end
task :jekyll => '_site/index.html'