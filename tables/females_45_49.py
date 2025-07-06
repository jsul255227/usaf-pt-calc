# females_45_49.py
# Official USAF PT scoring tables for Females Age 45-49
# Template based on previous age groups. Fill in each component as official values are provided.

# Helper function: Convert 'mm:ss' string to total seconds (int)
def mmss_to_seconds(mmss):
    """
    Convert a time string in 'mm:ss' format to total seconds.
    Example: '9:13' -> 553
    """
    m, s = map(int, mmss.split(':'))
    return m * 60 + s

# ----------------------
# Cardio: 1.5 Mile Run
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Lower time = higher score.
FEMALE_45_49_RUN = [
    (0, mmss_to_seconds('11:38') - 1, 60.0),                 # < 11:38
    (mmss_to_seconds('11:39'), mmss_to_seconds('12:14'), 59.5),
    (mmss_to_seconds('12:15'), mmss_to_seconds('12:33'), 59.0),
    (mmss_to_seconds('12:34'), mmss_to_seconds('12:53'), 58.5),
    (mmss_to_seconds('12:54'), mmss_to_seconds('13:14'), 58.0),
    (mmss_to_seconds('13:15'), mmss_to_seconds('13:36'), 57.5),
    (mmss_to_seconds('13:37'), mmss_to_seconds('14:00'), 57.0),
    (mmss_to_seconds('14:01'), mmss_to_seconds('14:25'), 56.5),
    (mmss_to_seconds('14:26'), mmss_to_seconds('14:52'), 56.0),
    (mmss_to_seconds('14:53'), mmss_to_seconds('15:20'), 55.5),
    (mmss_to_seconds('15:21'), mmss_to_seconds('15:50'), 55.0),
    (mmss_to_seconds('15:51'), mmss_to_seconds('16:22'), 54.5),
    (mmss_to_seconds('16:23'), mmss_to_seconds('16:57'), 54.0),
    (mmss_to_seconds('16:58'), mmss_to_seconds('17:34'), 53.5),
    (mmss_to_seconds('17:35'), mmss_to_seconds('18:14'), 52.0),
    (mmss_to_seconds('18:15'), mmss_to_seconds('18:56'), 50.5),
    (mmss_to_seconds('18:57'), mmss_to_seconds('19:43'), 48.0),
    (mmss_to_seconds('19:44'), mmss_to_seconds('20:33'), 45.0),
    (mmss_to_seconds('20:34'), mmss_to_seconds('21:28'), 42.0),
    (mmss_to_seconds('21:29'), mmss_to_seconds('22:28'), 38.5),
    (mmss_to_seconds('22:29'), mmss_to_seconds('23:34'), 35.0), # 23:34*
]

# ----------------------
# Cardio: HAMR (shuttles)
# ----------------------
# Each tuple: (start_shuttles, end_shuttles, score)
# Ranges are inclusive. Higher shuttles = higher score.
FEMALE_45_49_HAMR = [
    (69, float('inf'), 60.0),         # > 68
    (62, 68, 59.5),
    (59, 61, 59.0),
    (56, 58, 58.5),
    (54, 55, 58.0),
    (51, 53, 57.5),
    (48, 50, 57.0),
    (45, 47, 56.5),
    (42, 44, 56.0),
    (39, 41, 55.5),
    (36, 38, 55.0),
    (33, 35, 54.5),
    (30, 32, 54.0),
    (27, 29, 53.5),
    (24, 26, 52.0),
    (22, 23, 50.5),
    (19, 21, 48.0),
    (16, 18, 45.0),
    (13, 15, 42.0),
    (10, 12, 38.5),
    (7, 9, 35.0),                  # 7*-9
]
# ----------------------
# Strength: 1 min Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_45_49_PUSHUPS = [
    (38, float('inf'), 20.0),      # > 37
    (36, 37, 19.8),
    (35, 35, 19.6),
    (34, 34, 19.4),
    (33, 33, 19.2),
    (32, 32, 19.0),
    (31, 31, 18.8),
    (30, 30, 18.6),
    (29, 29, 18.4),
    (28, 28, 18.2),
    (27, 27, 18.0),
    (26, 26, 17.8),
    (25, 25, 17.6),
    (24, 24, 17.4),
    (23, 23, 17.2),
    (22, 22, 17.0),
    (21, 21, 16.8),
    (20, 20, 16.6),
    (19, 19, 16.4),
    (18, 18, 16.2),
    (17, 17, 16.0),
    (16, 16, 15.6),
    (15, 15, 15.0),
    (14, 14, 14.0),
    (13, 13, 13.0),
    (12, 12, 12.0),
    (11, 11, 11.0),
    (10, 10, 10.0),
    (9, 9, 7.0),
    (8, 8, 4.0),
    (7, 7, 1.0),                # 7*
]
# ----------------------
# Strength: 2 min Hand Release Push-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_45_49_HR_PUSHUPS = [
    (29, float('inf'), 20.0),      # > 28
    (27, 28, 19.6),
    (26, 26, 19.2),
    (25, 25, 18.8),
    (24, 24, 18.4),
    (23, 23, 18.0),
    (22, 22, 17.6),
    (21, 21, 17.2),
    (20, 20, 16.8),
    (19, 19, 16.4),
    (18, 18, 16.0),
    (17, 17, 15.6),
    (16, 16, 15.2),
    (15, 15, 14.8),
    (14, 14, 14.4),
    (13, 13, 14.0),
    (12, 12, 13.6),
    (11, 11, 13.2),
    (10, 10, 12.8),
    (9, 9, 12.4),
    (8, 8, 12.0),
    (7, 7, 11.6),
    (6, 6, 11.2),
    (5, 5, 10.8),
    (4, 4, 10.0),                # 4*
]
# ----------------------
# Strength: 1 min Sit-ups
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_45_49_SITUPS = [
    (36, float('inf'), 20.0),      # > 35
    (34, 35, 19.7),
    (33, 33, 19.4),
    (32, 32, 19.0),
    (31, 31, 18.8),
    (30, 30, 18.0),
    (29, 29, 17.6),
    (28, 28, 17.0),
    (27, 27, 16.6),
    (26, 26, 16.0),
    (25, 25, 15.0),
    (24, 24, 14.0),
    (23, 23, 13.0),
    (22, 22, 12.0),
    (21, 21, 9.0),
    (20, 20, 6.0),
    (19, 19, 3.0),                # 19*
]
# ----------------------
# Strength: 2 min Cross Leg Reverse Crunch
# ----------------------
# Each tuple: (start_reps, end_reps, score)
# Ranges are inclusive. Higher reps = higher score.
FEMALE_45_49_CRUNCH = [
    (41, float('inf'), 20.0),      # > 40
    (39, 40, 19.7),
    (38, 38, 19.4),
    (37, 37, 19.1),
    (36, 36, 18.8),
    (35, 35, 18.5),
    (34, 34, 18.2),
    (33, 33, 17.9),
    (32, 32, 17.6),
    (31, 31, 17.4),
    (30, 30, 17.1),
    (29, 29, 16.8),
    (28, 28, 16.5),
    (27, 27, 16.2),
    (26, 26, 15.9),
    (25, 25, 15.6),
    (24, 24, 15.3),
    (23, 23, 15.0),
    (22, 22, 14.7),
    (21, 21, 14.4),
    (20, 20, 14.1),
    (19, 19, 13.8),
    (18, 18, 13.5),
    (17, 17, 13.2),
    (16, 16, 12.9),
    (15, 15, 12.6),
    (14, 14, 12.4),
    (13, 13, 12.1),
    (12, 12, 11.8),
    (11, 11, 11.5),
    (10, 10, 11.2),
    (9, 9, 10.9),
    (8, 8, 10.6),
    (7, 7, 10.3),
    (6, 6, 10.0),                # 6*
]
# ----------------------
# Forearm Plank (seconds)
# ----------------------
# Each tuple: (start_seconds, end_seconds, score)
# Ranges are inclusive. Higher time = higher score.
FEMALE_45_49_PLANK = [
    (mmss_to_seconds('3:06'), float('inf'), 20.0),      # > 3:05
    (mmss_to_seconds('3:00'), mmss_to_seconds('3:05'), 19.7),
    (mmss_to_seconds('2:54'), mmss_to_seconds('2:59'), 19.3),
    (mmss_to_seconds('2:47'), mmss_to_seconds('2:53'), 18.8),
    (mmss_to_seconds('2:40'), mmss_to_seconds('2:46'), 18.4),
    (mmss_to_seconds('2:20'), mmss_to_seconds('2:39'), 17.1),
    (mmss_to_seconds('2:00'), mmss_to_seconds('2:19'), 15.8),
    (mmss_to_seconds('1:40'), mmss_to_seconds('1:59'), 14.5),
    (mmss_to_seconds('1:20'), mmss_to_seconds('1:39'), 13.2),
    (mmss_to_seconds('1:00'), mmss_to_seconds('1:19'), 11.9),
    (mmss_to_seconds('0:40'), mmss_to_seconds('0:59'), 10.6),
    (mmss_to_seconds('0:35'), mmss_to_seconds('0:39'), 10.3),
    (mmss_to_seconds('0:30'), mmss_to_seconds('0:34'), 10.0),   # 0:30*
]
# ----------------------
# Add additional component tables below as official values are provided.
# ----------------------
