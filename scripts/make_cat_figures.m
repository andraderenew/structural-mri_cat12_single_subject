clear;
clc;

project = '/Users/andraderenew/github/structural-mri_cat12_single_subject';

spmroot = '/Users/andraderenew/toolboxes/spm_25.01.02';
addpath(spmroot, '-begin');

spm('defaults', 'fmri');

cat_anat = fullfile(project, ...
    'data/raw/derivatives/CAT26.0.rc3_3250/sub-01/ses-test/anat');

original = fullfile(project, ...
    'data/raw/sub-01/ses-test/anat/sub-01_ses-test_T1w.nii');

files = {
    original
    fullfile(cat_anat, 'p0sub-01_ses-test_T1w.nii')
    fullfile(cat_anat, 'mwp1sub-01_ses-test_T1w.nii')
    fullfile(cat_anat, 'mwp2sub-01_ses-test_T1w.nii')
    fullfile(cat_anat, 's6mwp1sub-01_ses-test_T1w.nii')
};

outputs = {
    'fig2_original_t1.png'
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
