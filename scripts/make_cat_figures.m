clear;
clc;

script_path = mfilename('fullpath');
script_dir = fileparts(script_path);
project = fileparts(script_dir);

project_env = getenv('CAT_PROJECT_ROOT');
if ~isempty(project_env)
    project = project_env;
end

spmroot = getenv('SPM25_ROOT');
if isempty(spmroot)
    error(['SPM25_ROOT is not set. Point it to the SPM25 installation ', ...
           'that contains spm.m.']);
end

if ~isfile(fullfile(spmroot, 'spm.m'))
    error('SPM25_ROOT does not contain spm.m: %s', spmroot);
end

addpath(spmroot, '-begin');

spm('defaults', 'fmri');

cat_anat = fullfile(project, ...
    'data/raw/derivatives/CAT26.0.rc3_3250/sub-01/ses-test/anat');

% The original T1 figure is generated independently by:
%   scripts/make_original_t1_figure.py
%
% The CAT-derived NIfTI files below are not distributed in the repository.
% These entries reproduce the historical SPM display workflow when the
% original CAT derivatives are available.

files = {
    fullfile(cat_anat, 'p0sub-01_ses-test_T1w.nii')
    fullfile(cat_anat, 'mwp1sub-01_ses-test_T1w.nii')
    fullfile(cat_anat, 'mwp2sub-01_ses-test_T1w.nii')
    fullfile(cat_anat, 's6mwp1sub-01_ses-test_T1w.nii')
};

outputs = {
    'fig3_cat_segmentation.png'
    'fig4_modulated_normalized_gm.png'
    'fig5_modulated_normalized_wm.png'
    'fig6_smoothed_gm_6mm.png'
};

outdir = fullfile(project, 'results', 'figures');

for i = 1:numel(files)

    if ~isfile(files{i})
        warning('No encontrado: %s', files{i});
        continue;
    end

    spm_check_registration([files{i} ',1']);
    drawnow;

    h = spm_figure('GetWin', 'Graphics');

    exportgraphics( ...
        h, ...
        fullfile(outdir, outputs{i}), ...
        'Resolution', 200);

    fprintf('Guardada: %s\n', outputs{i});
end

fprintf('\nFiguras terminadas en:\n%s\n', outdir);
