function h5write_ds(h5_path, ds_path, data)
    h5_path = get_absolute_path(h5_path);
    h5create(h5_path, ds_path, size(data));
    h5write(h5_path, ds_path, data)
end
