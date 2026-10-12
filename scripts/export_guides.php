<?php
require 'components/Services/Localisation/UiPhrasebook.php';
use Components\Services\Localisation\UiPhrasebook as P;
$clean = function ($v) use (&$clean) {
    if (is_string($v)) return P::without_keys($v);
    if (is_array($v)) return array_map($clean, $v);
    return $v;
};
$o = [];
foreach (glob('resources/guides/entries/*.php') as $f) {
    $g = require $f;
    if (($g['published'] ?? true) === false) continue;
    $o[] = $clean(['slug' => $g['slug'], 'title' => $g['title'], 'summary' => $g['summary'],
        'family' => $g['family'] ?? '', 'audience' => $g['audience'] ?? '', 'agent_paths' => $g['agent_paths'] ?? null]);
}
echo json_encode($o, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE);
