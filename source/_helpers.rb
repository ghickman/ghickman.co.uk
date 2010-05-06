module Helpers

  def category_slug(cat)
    cat.downcase.gsub(/[^A-Za-z0-9.\-]/, '-')
  end

  def category_capitalize(cat);
    cat.split(' ').map(&:capitalize).join(' ')
  end

  def category_list(categories)
    categories.map { |cat|
      %Q{ <a href="/category/#{category_slug(cat)}">#{category_capitalize(cat)}</a> }
    }.join(', ')
  end

end