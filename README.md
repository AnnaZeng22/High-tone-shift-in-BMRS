# High-tone-shift-in-BMRS
a BMRS grammar models high tone shift based on the pattern in Kibondei

Elements may be high-toned H, low-toned L, or unspecified for tone 0. As a simplification, you may assume that no more than one high-toned element is present in the
input.

1. Elements may be high-toned H, low-toned L, or unspecified for tone 0. As a simplification, you may assume that no more than one high-toned element is present in the input.
2. All low-toned elements in the input surface as low-toned in the output L → L; L cannot shift to H,L cannot shift to 0
3. High tones shift to the penultimate element if possible H000→00H0. High tones can only replace unspecified elements and they leave a unspecified element behind.
4. High tones cannot shift across low tones. If a low-toned element in the input intervenes between a high tone and the penultimate element, it only shifts up to the low-toned element: H000L000 → 000HL000; H000L000 cannot shift to 0000L0H0.
5. High tones cannot surface on the final element. Underlyingly final high tones shift to the penult if possible 000H→00H0, and delete if it is occupied by a low tone: 00LH →00L0; 00LH cannot shift to 0HL0

Note: adapted from UCL PLIN0034 coursework
