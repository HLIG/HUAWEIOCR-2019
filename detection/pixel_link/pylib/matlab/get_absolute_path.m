function abs_path = get_absolute_path(p)
    cur = pwd;
    [target_path, file_name, ext] = fileparts(p);
    cd(target_path);
    abs_path = pwd;
    cd(cur);
    
    abs_path = fullfile(abs_path, sprintf('%s%s', file_name, ext));
end
